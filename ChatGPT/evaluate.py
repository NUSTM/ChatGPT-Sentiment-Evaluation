import openai
import os
import argparse
import random
import numpy as np
import time
import backoff
import json


openai.api_key = "api-token"

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_tokens", type=int, help="Max tokens to be generated")
    parser.add_argument("--temperature", type=float, help="Temperature of the model")
    parser.add_argument("--top_p", type=float, help="Top p of the model")
    parser.add_argument("--top_k", type=int, help="Top k of the model")
    parser.add_argument("--seed", type=int, default = 42, help="random seed")

    parser.add_argument("--do_zero_shot", default = True, action="store_true", help="do zero-shot evaluation")
    parser.add_argument("--do_few_shot", action="store_true", help="do few-shot evaluation")

    parser.add_argument("--shot_num", type=int, default = 0)
    parser.add_argument("--task", type = str, default = "ASPE")
    parser.add_argument("--dataset", type = str, default = "14res")

    parser.add_argument("--llm_name", type=str, default = "gpt-3.5-turbo", help = "the name of LLM")
    parser.add_argument("--file_prefix", type=str)
    parser.add_argument("--test_file", type=str, default = "100_test")

    args = parser.parse_args()
    return args

def setup_seed(seed):
    np.random.seed(seed)
    random.seed(seed)


def read_line_examples_from_file(data_path):
    """
    Read data from file, each line is: sent####labels
    Return List[List[word]], List[Tuple]
    """
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        words, labels = [], []
        for line in fp:
            line = line.strip()
            if line != '':
                text, tuples = line.split('####')
                sents.append(text.strip())
                labels.append(eval(tuples))
    print(f"total examples = {len(sents)}")
    return sents, labels


def get_response(llm_name, task_prompt, query_input, do_few_shot, few_shot_sents = None, few_shot_labels = None, few_shot_explanations = None):    
    our_messages = [{"role": "system", "content": task_prompt}]
    if do_few_shot:
        for idx, sent in enumerate(few_shot_sents):
            label = few_shot_labels[idx]
            explanation = few_shot_explanations[idx]
            our_messages.append({"role": "system", "name":"example_user", "content": "Review: " + sent})
            our_messages.append({"role": "system", "name": "example_assistant", "content": "Label: " + str(label) + "\n" + "Explanation: " + explanation})
    our_messages.append({"role": "user", "content": query_input})
    # print(our_messages)
    response = openai.ChatCompletion.create(
        model = llm_name,
        messages = our_messages,
        temperature = 0
    )
    # print(response)
    return response["choices"][0]["message"]["content"]

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def get_response_with_backoff(llm_name, task_prompt, query_input, do_few_shot, few_shot_sents = None, few_shot_labels = None, few_shot_explanations = None):
    return get_response(llm_name, task_prompt, query_input, do_few_shot, few_shot_sents, few_shot_labels, few_shot_explanations)

def evaluate(args, task_prompt, log_file_path, result_file_path):
    log_file = open(log_file_path, 'w+', encoding='utf-8')
    res_file = open(result_file_path, 'w+', encoding='utf-8')

    data_dir = f'./data/{args.task}/{args.dataset}/'
    if args.do_few_shot:
        train_sents, train_labels = read_line_examples_from_file(data_dir + "train.txt")
        few_shot_idxs = np.random.randint(0, len(train_sents), args.shot_num)
        # print(few_shot_idxs)
        demo_dict = {}
        with open("./data/ASPE/14res/demo.json") as fin:
            d_dict = json.load(fin)
        for item in d_dict:
            demo_dict[str(item['idx'])] = item
        demo_explanations = [demo_dict[str(i)]['explanation'] for i in few_shot_idxs]
        demo_sents = [train_sents[i] for i in few_shot_idxs]
        demo_labels = [train_labels[i] for i in few_shot_idxs]
    else:
        demo_sents, demo_labels = [], []

    # demo_sents = ['But the staff was so horrible to us.', "Best of all is the warm vibe , the owner is super friendly and service is fast .", "Nevertheless the food itself is pretty good .", "Faan 's got a great concept but a little rough on the delivery .", "The fried rice is amazing here ."]
    # demo_labels = [[('staff', 'negative')], [('vibe', 'positive'), ('owner', 'positive'), ('service', 'positive')], [('food', 'positive')], [('delivery', 'negative')], [('fried rice', 'positive')]]

    test_sents, test_labels = read_line_examples_from_file(data_dir + f"{args.test_file}.txt")
    print(f"total test examples = {len(test_sents)}")
    print(f"shot_num = {args.shot_num}")
    if args.do_few_shot:
        print("*"*15 + "few-shot evaluation" + "*"*15)
        for i in range(len(demo_sents)):
            print("*"*5)
            print(f"Review#{i}:{demo_sents[i]}\nLabel#{i}:{demo_labels[i]}\nExplanation{i}:{demo_explanations[i]}")

    for idx, sent in enumerate(test_sents):
        if args.task == "ABSC":
            cur_label = test_labels[idx]
            assert len(cur_label) == 2
            aspect = cur_label[0]
            query_input = f"Sentence: {sent} What is the sentiment polarity of the aspect {aspect} in this sentence?"
        elif args.task == "ASPE":
            query_input = "Review: " + sent
        else:
            query_input = sent
        response = get_response_with_backoff(args.llm_name, task_prompt, query_input, args.do_few_shot, few_shot_sents = demo_sents, few_shot_labels = demo_labels, few_shot_explanations = demo_explanations) 
        print("*"*30 + str(idx) + "*"*30)
        print(task_prompt)
        print(response)
        print(f"GT:{test_labels[idx]}")
        log_file.write(f"{'*'*30 + str(idx) + '*'*30}\n{task_prompt}\n{response}\nGT:{test_labels[idx]}\n")
        res_file.write(sent + "####" + response.replace("\n", "") + "\n")
        time.sleep(10)
    log_file.close()
    res_file.close()
    print("Done")
    


if __name__ == '__main__':
    args = init_args()
    setup_seed(args.seed)

    # task_prompt = "I want you to act as an annotator for the Aspect-Based Sentiment Analysis task. I will provide you with a customer review, and you will understand it, extract the aspect terms and predict the corresponding sentiment polarity in this review. Make sure that the aspect terms are present in the review. I want you to only predict the results without giving extra text or explanations."
    task_prompt = "Given a review, extract the aspect term(s) and determine their corresponding sentiment polarity."
    data_dir = f'./data/{args.task}/{args.dataset}/'
    log_file_path = data_dir + f"{args.file_prefix}_log.txt"
    result_file_path = data_dir + f"{args.file_prefix}_results.txt"
    evaluate(args, task_prompt, log_file_path, result_file_path)
