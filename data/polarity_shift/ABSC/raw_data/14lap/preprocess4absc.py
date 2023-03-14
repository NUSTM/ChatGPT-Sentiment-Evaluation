sentimenttag2word = {"NEG": 'negative', "NEU": 'neutral', "POS": 'positive'}


def extract_text_and_labels(tokens_ls, labels_ls):
    pairs = []
    text = " ".join(tokens_ls)
    
    i = 0
    while i < len(labels_ls):
        if labels_ls[i] != "O":
            aspect_words = tokens_ls[i]
            _, sentiment_tag = labels_ls[i].split("-")
            sentiment_word = sentimenttag2word[sentiment_tag]

            flag = 0
            j = i + 1
            if j == len(labels_ls):
                pairs.append([aspect_words, sentiment_word])
                break
            else:
                while j < len(labels_ls):
                    if labels_ls[j] == "O":
                        flag = 1
                        pairs.append([aspect_words, sentiment_word])
                        break
                    else:
                        aspect_words += " "
                        aspect_words += tokens_ls[j]
                        _, next_sentiment_tag = labels_ls[j].split("-")
                        sentiment_word = sentimenttag2word[next_sentiment_tag]
                        j += 1
                i = j + 1
        else:
            i += 1
    return text, pairs


def read_line_examples_from_raw_dataset_file(data_path, silence=True):
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        tokens_ls, labels_ls = [], []
        for line in fp:
            if line != '':
                if line == "\n":
                    text, pairs = extract_text_and_labels(tokens_ls, labels_ls)
                    if len(pairs) > 0:
                        for pair in pairs:
                            sents.append(text)
                            labels.append([pair])
                    tokens_ls.clear()
                    labels_ls.clear()
                else:
                    token, label = line.split(" ")
                    token = token.strip()
                    label = label.strip()
                    tokens_ls.append(token)
                    labels_ls.append(label)
    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, target_path):
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    for i in range(len(sents)):
        # print(i)
        # print(sents[i])
        # print(labels[i])
        # print(target_path)
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
    new_file.close()
    print(f'{target_path} has been generated!')


def convert_idx_format_to_text_format_for_absc(datasets):  
    for dataset in datasets:
        for split in ['dev', 'test']:
            for ps_type in ["neg", "spec"]:
                prefix_path = f'../../{dataset}/'
                cur_file_path = f'./{split}_{ps_type}.txt'
                sents, labels = read_line_examples_from_raw_dataset_file(cur_file_path, silence=True)
                target_path = f'{prefix_path}{split}_{ps_type}.txt'
                write_file_given_sents_labels(sents, labels, target_path)
    

if __name__ == '__main__':
    datasets = ['14lap']
    convert_idx_format_to_text_format_for_absc(datasets)