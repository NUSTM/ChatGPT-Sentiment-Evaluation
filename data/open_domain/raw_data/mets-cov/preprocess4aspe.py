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
                sample = line.split('\t')

                words = sample[1].split(' ')

                labels_seq = sample[2]
                labels_seq_ls = labels_seq.split("}, {")
                for label_seq in labels_seq_ls:
                    label_seq = label_seq.replace("[{", "").replace("}]", "")
                    label_ls = label_seq.split(", ")
                    for label in label_ls:
                        if label.startswith("'value': "):
                            _, aspect_words = label.split("'value': ")
                            aspect_words = aspect_words.replace("\'", "")
                            aspect_words = aspect_words.strip()
                        if label.startswith("'sentiment': "):
                            _, sentiment_word = label.split("'sentiment': ")
                            sentiment_word = sentiment_word.replace("\'", "").replace("\"", "")
                            sentiment_word = sentiment_word.strip()
                            if sentiment_word != "null":
                                sentiment_word = sentiment_dic[sentiment_word]
                                pairs.append([aspect_words, sentiment_word])
                if len(pairs) > 0:
                    sents.append(sample[1])
                    labels.append(pairs) 
    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, target_path):
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    for i in range(len(sents)):
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
    new_file.close()
    print(f'{target_path} has been generated!')


def convert_idx_format_to_text_format_for_aspe(datasets):
    prefix_path = '../../ASPE/'  
    for dataset in datasets:
        for split in ['train', 'dev', 'test']:
            cur_file_path = f'./{split}.txt'
            sents, labels = read_line_examples_from_raw_dataset_file(cur_file_path, silence=True)
            target_path = f'{prefix_path}{dataset}/{split}.txt'
            write_file_given_sents_labels(sents, labels, target_path)
    

if __name__ == '__main__':
    datasets = ['mets-cov']
    convert_idx_format_to_text_format_for_aspe(datasets)