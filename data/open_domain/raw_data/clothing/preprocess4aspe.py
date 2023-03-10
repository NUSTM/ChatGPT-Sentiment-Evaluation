sentiment = ['negative', 'neutral', 'positive']


def read_line_examples_from_raw_acos_dataset_file(data_path, silence=True):
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        for line in fp:
            words, pairs = [], []
            line = line.strip()
            if line != '':
                sample = line.split('\t')

                words = sample[0].split(' ')

                a_ls, s_ls = [], []
                for quad in sample[1:]:
                    quad = quad.split(' ')
                    start, end = int(quad[0].split(',')[0]), int(quad[0].split(',')[1])
                    if start != -1 and end != -1:
                        aspect_words = ' '.join(words[start:end])
                        sentiment_word = sentiment[int(quad[2])]
                    
                        if a_ls.count(aspect_words) == 0:
                            a_ls.append(aspect_words)
                            s_ls.append(sentiment_word)
                            pairs.append([aspect_words, sentiment_word])
                if len(pairs) > 0:
                    sents.append(sample[0])
                    labels.append(pairs) 
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
    prefix_path = '../../ASPE/'  
    for dataset in datasets:
        for split in ['train', 'dev', 'test']:
            cur_file_path = f'./{split}.txt'
            sents, labels = read_line_examples_from_raw_acos_dataset_file(cur_file_path, silence=True)
            target_path = f'{prefix_path}{dataset}/{split}.txt'
            write_file_given_sents_labels(sents, labels, target_path)
    

if __name__ == '__main__':
    datasets = ['clothing']
    convert_idx_format_to_text_format_for_aspe(datasets)