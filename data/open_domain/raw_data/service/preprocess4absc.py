sentitag2label = {"T-POS": "positive", "T-NEG": "negative", "T-NEU": "neutral"}


def extract_labels(word_ls, label_seq):
    idx_ls, senti_ls, pairs = [], [], []
    label_seq_ls = label_seq.split(" ")
    i = 0
    while i < len(label_seq_ls):
        label_seq = label_seq_ls[i]
        if label_seq.find("T-") != -1:
            aspect_words = word_ls[i]
            label = label_seq[label_seq.find("T-"):]
            sentiment_word = sentitag2label[label]

            flag = 0
            j = i + 1
            if j == len(label_seq_ls):
                pairs.append([aspect_words, sentiment_word])
                break
            else:
                while j < len(label_seq_ls):
                    next_label_seq = label_seq_ls[j]
                    if next_label_seq.find("T-") == -1:
                        flag = 1
                        pairs.append([aspect_words, sentiment_word])
                        break
                    else:
                        aspect_words += " "
                        aspect_words += word_ls[j]
                        next_label = next_label_seq[next_label_seq.find("T-"):]
                        sentiment_word = sentitag2label[next_label]
                        j += 1
                i = j + 1
        else:
            i += 1
    return pairs


def read_line_examples_from_raw_dataset_file(data_path, silence=True):
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        for line in fp:
            words, pairs = [], []
            line = line.strip()
            if line != '':
                sample = line.split('####')

                words = sample[0].split(' ')

                pairs = extract_labels(words, sample[1])
                if len(pairs) > 0:
                    for pair in pairs:
                        sents.append(sample[0])
                        labels.append(pair) 
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


def convert_idx_format_to_text_format_for_aspe(datasets):
    prefix_path = '../../ABSC/'  
    for dataset in datasets:
        for split in ['train', 'test']:
            cur_file_path = f'./{split}.txt'
            sents, labels = read_line_examples_from_raw_dataset_file(cur_file_path, silence=True)
            target_path = f'{prefix_path}{dataset}/{split}.txt'
            write_file_given_sents_labels(sents, labels, target_path)
    

if __name__ == '__main__':
    datasets = ['service']
    convert_idx_format_to_text_format_for_aspe(datasets)