from chatgpt_wrapper import ChatGPT
import time

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



if __name__ == '__main__':
    test_path = "data/ASPE/14lap/100_test.txt"

    sents, labels = read_line_examples_from_file(test_path)
    # print(len(sents), len(labels))
    bot = ChatGPT()
    # test code
    # prompt = "hello!"
    # response = bot.ask(prompt)
    # print(response)  # prints the response from 

    log_file = open(test_path.split(".")[0] + "_log.txt", 'w+', encoding='utf-8')
    for idx, sent in enumerate(sents):
        bot.new_conversation()
        task_prompt = f"Given a sentence or text, extract the aspect term(s) and determine their corresponding sentiment polarity. Text: {sent}"
        # task_prompt = f"Identify the aspect term(s) and sentiment polarity in a product review or feedback. Review: {sent}"
        # task_prompt = f"Analyze the aspect term(s) and sentiment polarity in a social media post or tweet related to a topic or subject. Post: {sent}"
        response = bot.ask(task_prompt)
        print("*"*30 + str(idx) + "*"*30)
        print(task_prompt)
        print(response)
        print(f"GT:{labels[idx]}")
        log_file.write(f"{'*'*30 + str(idx) + '*'*30}\n{task_prompt}\n{response}\nGT:{labels[idx]}\n")
        time.sleep(5)
    log_file.close()
