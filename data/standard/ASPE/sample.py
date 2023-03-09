'''
Author: SinclairCoder 1793140623@qq.com
Date: 2023-01-16 13:39:22
LastEditors: SinclairCoder 1793140623@qq.com
LastEditTime: 2023-02-28 02:36:50
FilePath: /ABSA-In-Domain-Pre-training/data4fewshot/generate_data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random
import os


seed_ls = []
ls = []

def read_line_examples_from_dataset_file(data_path, silence=True):
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        for line in fp:
            line = line.strip()
            text, label_list = line.split("####")
            sents.append(text)
            labels.append(label_list)
    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, number_list, target_path, random_seed):
    num_pos, num_neu, num_neg = 0, 0, 0 
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    for i in number_list:
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
        num_pos += labels[i].count("positive")
        num_neu += labels[i].count("neutral")
        num_neg += labels[i].count("negative")
    new_file.close()
    print(f'{target_path} has been generated!')
    print("pos:", num_pos, "neu:", num_neu, "neg:", num_neg)
    # return [num_pos, num_neu, num_neg]   
    # new_file.close()
    # print(f'{target_path} has been generated!')
    # print("pos:", num_pos, "neu:", num_neu, "neg:", num_neg)


def convert_idx_format_to_text_format(datasets, task_list, num_shot, random_seed, flag):
    global ls

    for task in task_list:
        for dataset in datasets:
            for split in ['test']:    
                prefix_path = os.path.abspath(os.path.join(os.getcwd(), "../."))
                cur_file_path = f"./{dataset}/{split}.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                
                target_path = f'./{dataset}/{num_shot}_{split}.txt'
                sents, labels = read_line_examples_from_dataset_file(cur_file_path, silence=True)
                number_list = random.sample(range(len(sents)), num_shot)
                write_file_given_sents_labels(sents, labels, number_list, target_path, random_seed)
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
    num_shot = 100
    for random_seed in [0]:
        datasets = ['14res']
        task_list = ['ASPE']
        flag = 1
        convert_idx_format_to_text_format(datasets, task_list, num_shot, random_seed, flag)

    # print(seed_ls)