import random


pos_idx_ls, neg_idx_ls, neu_idx_ls, sample_idx_ls = [], [], [], []
random.seed(29)


def read_line_examples_from_dataset_file(data_path, silence=True):
    sents, labels = [], []
    n = 0
    with open(data_path, 'r', encoding='UTF-8') as fp:
        for line in fp:
            line = line.strip()
            text, label_list = line.split("####")
            sents.append(text)
            labels.append(label_list)
            if label_list.count("positive") > 0:
                pos_idx_ls.append(n)
            elif label_list.count("negative") > 0:
                neg_idx_ls.append(n)
            elif label_list.count("neutral") > 0:
                neu_idx_ls.append(n)
            n += 1
    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, idx_list, target_path):
    num_pos, num_neu, num_neg = 0, 0, 0 
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    for i in idx_list:
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
        num_pos += labels[i].count("positive")
        num_neu += labels[i].count("neutral")
        num_neg += labels[i].count("negative")
    new_file.close()
    print(f'{target_path} has been generated!')
    print("pos:", num_pos, "neu:", num_neu, "neg:", num_neg)


def convert_idx_format_to_text_format(datasets, num_pos, num_neg, num_neu):
    for dataset in datasets:
        for split in ['test']:    
            cur_file_path = f"./{split}.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                
            target_path = f'./{num_pos + num_neg + num_neu}_{split}.txt'
            sents, labels = read_line_examples_from_dataset_file(cur_file_path, silence=True)
            sample_idx_ls.extend(random.sample(pos_idx_ls, num_pos))
            sample_idx_ls.extend(random.sample(neg_idx_ls, num_neg))
            if num_neu > 0:
                sample_idx_ls.extend(random.sample(neu_idx_ls, num_neu))
            sample_idx_ls.sort()
            write_file_given_sents_labels(sents, labels, sample_idx_ls, target_path)


if __name__ == '__main__':
    # num_pos, num_neg, num_neu = 10, 7, 3
    num_pos, num_neg, num_neu = 15, 10, 5
    datasets = ['financial']
    convert_idx_format_to_text_format(datasets, num_pos, num_neg, num_neu)