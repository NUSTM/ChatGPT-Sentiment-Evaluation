'''
Author: SinclairCoder 1793140623@qq.com
Date: 2023-02-28 02:49:38
LastEditors: SinclairCoder 1793140623@qq.com
LastEditTime: 2023-02-28 07:07:55
FilePath: /data4/ChatGPT_eval/data/SST2/load_data.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import datasets
from transformers import AutoTokenizer


# sentiid2sentilabel = {"0": "negative", "1": "positive"}
pos_idx, neg_idx = [], []
num_sample = 100


def download_data():
    sents, labels = [], []
    dataset = datasets.load_dataset("sst2")
    val_data = dataset["validation"]
    for idx in range(len(val_data)):
        sents.append(val_data[idx]["sentence"])
        labels.append(val_data[idx]["label"])
        # if len(neg_idx) < (num_sample / 2) and val_data[idx]["label"] == 0:
        #     neg_idx.append(idx)
        # if len(pos_idx) < (num_sample / 2) and val_data[idx]["label"] == 1:
        #     pos_idx.append(idx)

    return sents, labels


def write_file_given_sents_labels(sents, labels, target_path):
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    num_pos, num_neg = 0, 0
    for i in range(len(sents)):
        new_file.write(sents[i]+'####'+str(labels[i])+'\n')
        if labels[i] == 0:
            num_neg += 1
        else:
            num_pos += 1
    new_file.close()
    print(f'{target_path} has been generated!')
    print("pos:", num_pos, "neg:", num_neg)


if __name__ == "__main__":
    sents, labels = download_data()
    target_path = f"./dev.txt"
    # test_idx = pos_idx + neg_idx
    # test_idx.sort()
    write_file_given_sents_labels(sents, labels, target_path)