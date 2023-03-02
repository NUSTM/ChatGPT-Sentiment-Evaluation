'''
Author: SinclairCoder 1793140623@qq.com
Date: 2023-01-16 13:39:22
LastEditors: SinclairCoder 1793140623@qq.com
LastEditTime: 2023-03-02 09:35:56
FilePath: /ABSA-In-Domain-Pre-training/data4fewshot/generate_data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random
import os

## 14-lap-50
# num_sample = 50
# num_pos = 27
# num_neg = 10
# num_neu = 13
## 14-lap-100
# num_sample = 100
# num_pos = 54
# num_neg = 20
# num_neu = 26
## 14-res-50
# num_sample = 50
# num_pos = 32
# num_neg = 9
# num_neu = 9
## 14-res-100
num_sample = 100
num_pos = 66
num_neg = 17
num_neu = 17

pos_idx, neg_idx, neu_idx = [], [], []


def read_line_examples_from_dataset_file(data_path, silence=True):
    sents, labels = [], []
    idx = 0
    with open(data_path, 'r', encoding='UTF-8') as fp:
        for line in fp:
            line = line.strip()
            text, label_list = line.split("####")           
            sents.append(text)
            labels.append(label_list)
            if len(neg_idx) < num_neg and label_list.find("negative") != -1:
                neg_idx.append(idx)
            if len(pos_idx) < num_pos and label_list.find("positive") != -1:
                pos_idx.append(idx)
            if len(neu_idx) < num_neu and label_list.find("neutral") != -1:
                neu_idx.append(idx)
            idx += 1

    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, test_idx, target_path):
    n_pos, n_neg, n_neu = 0, 0, 0
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    for i in test_idx:
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
        n_pos += labels[i].count("positive")
        n_neg += labels[i].count("negative")
        n_neu += labels[i].count("neutral")

    new_file.close()
    print(f'{target_path} has been generated!')
    print("pos:", n_pos, "neg:", n_neg, "neu:", n_neu)
    # return [num_pos, num_neu, num_neg]   
    # new_file.close()
    # print(f'{target_path} has been generated!')
    # print("pos:", num_pos, "neu:", num_neu, "neg:", num_neg)


def convert_idx_format_to_text_format(datasets, task_list):
    global ls

    for task in task_list:
        for dataset in datasets:
            for split in ['test']:    
                cur_file_path = f"./{dataset}/{split}.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                
                target_path = f'./{dataset}/{num_sample}_{split}.txt'
                sents, labels = read_line_examples_from_dataset_file(cur_file_path, silence=True)
                test_idx = pos_idx + neg_idx + neu_idx
                test_idx.sort()
                write_file_given_sents_labels(sents, labels, test_idx, target_path)
    #             ls.append(write_file_given_sents_labels(sents, labels, number_list, target_path, random_seed))
    # if flag == 1:
    #     num = 0
    #     for i in range(len(ls)):
    #         if 0 in ls[i]:
    #             num += 1
    #             break
    #     if num == 0:
    #         seed_ls.append(random_seed)
    #     ls.clear()
    

if __name__ == '__main__':
    datasets = ['14res']
    task_list = ['ASPE']
    convert_idx_format_to_text_format(datasets, task_list)
