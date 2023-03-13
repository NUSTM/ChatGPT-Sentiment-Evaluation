import re
sentiment_dic = {"Negative": 'negative', "Neutral": 'neutral', "Positive": 'positive'}


def read_line_examples_from_raw_dataset_file(data_path, silence=True):
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        i = 0
        for line in fp:
            if i == 0:
                i += 1
                continue
            words, pairs = [], []
            line = line.strip()
            if line != '':
                idx_text, labels_num = line.split(",\"{")
                if len(re.split("[0-9],", idx_text)) > 2:
                    text = "".join(re.split("[0-9],", idx_text)[1:])
                else:
                    text = re.split("[0-9],", idx_text)[-1]
                # print(text)
                labels_seq = re.split(",[0-9]", labels_num)[0]

                words = text.replace("\"", "").replace("\'", "").split(' ')

                # ""Gold"": ""positive"", ""Silver"": ""negative""}"
                labels_seq_ls = labels_seq.split("\", \"")
                for label_seq in labels_seq_ls:
                    # print(label_seq)
                    aspect_words, sentiment_word = label_seq.split("\": \"")
                    aspect_words = aspect_words.replace("\"", "").replace("}", "")
                    aspect_words = aspect_words.strip()
                    sentiment_word = sentiment_word.replace("\"", "").replace("}", "")
                    sentiment_word = sentiment_word.strip()
                    pairs.append([aspect_words, sentiment_word])
                if len(pairs) > 0:
                    for pair in pairs:
                        sents.append(text.replace("\"", "").replace("\'", ""))
                        labels.append(pair) 
    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, target_path, split):
    start, end = 0, 0
    if split == "train":
        start = 0
        end = round(len(sents) * 0.7)
    elif split == "test":
        start = round(len(sents) * 0.7)
        end = start + round(len(sents) * 0.2)
    elif split == "dev":
        start = round(len(sents) * 0.9)
        end = start + round(len(sents) * 0.1)
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    for i in range(start, end):
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
    new_file.close()
    print(f'{target_path} has been generated!')


def convert_idx_format_to_text_format_for_aspe(datasets):
    prefix_path = '../../ABSC/'  
    for dataset in datasets:
        for split in ['train', 'test', 'dev']:
            cur_file_path = f'./all.txt'
            sents, labels = read_line_examples_from_raw_dataset_file(cur_file_path, silence=True)
            target_path = f'{prefix_path}{dataset}/{split}.txt'
            write_file_given_sents_labels(sents, labels, target_path, split)
    

if __name__ == '__main__':
    datasets = ['financial']
    convert_idx_format_to_text_format_for_aspe(datasets)