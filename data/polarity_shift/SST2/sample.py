neg_idx_ls, spec_idx_ls, sample_idx_ls = [], [], []
neg_seed_lexicon = ["n't", "no", "not", "never", "neither", "nor", "unless", "but", "however", "rather than", "not yet", "not only", "nonetheless", "despite", "although", "even though", "in spite of", "unlikely"]
spec_seed_lexicon = ["if", "would", "could", "should", "seems", "might", "maybe", "whether", "unless", "even if", "if only", "ca n't believe", "grant that", "guessing", "suspect", "hope", "wish", "let's", "probably"]


def read_line_examples_from_dataset_file(data_path, silence=True):
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        i = 0
        for line in fp:
            line = line.strip()
            text, label_list = line.split("####")

            for seed_word in neg_seed_lexicon:
                if text.find(" " + seed_word + " ") != -1 and neg_idx_ls.count(i) == 0:
                    neg_idx_ls.append(i)
            for seed_word in spec_seed_lexicon:
                if text.find(" " + seed_word + " ") != -1 and spec_idx_ls.count(i) == 0:
                    spec_idx_ls.append(i) 
            
            sents.append(text)
            labels.append(label_list)
            i += 1
    if silence:
        print(f"Total examples = {len(sents)}")
    return sents, labels


def write_file_given_sents_labels(sents, labels, target_path):
    new_file = open(target_path, 'w+', encoding = 'utf-8')
    if target_path.find("neg") != -1:
        for i in neg_idx_ls:
            new_file.write(sents[i]+'####'+str(labels[i])+'\n')
    else:
        for i in spec_idx_ls:
            new_file.write(sents[i]+'####'+str(labels[i])+'\n')
    new_file.close()
    print(f'{target_path} has been generated!')


def convert_idx_format_to_text_format(datasets):
    for dataset in datasets:
        for split in ['sst2_neg', 'sst2_spec']:    
            cur_file_path = f"./dev.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                
            target_path = f'./{split}.txt'
            sents, labels = read_line_examples_from_dataset_file(cur_file_path, silence=True)
            write_file_given_sents_labels(sents, labels, target_path)


if __name__ == '__main__':
    datasets = ['SST2']
    convert_idx_format_to_text_format(datasets)