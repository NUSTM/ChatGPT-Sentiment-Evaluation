import difflib
from nltk.util import ngrams
from fuzzywuzzy import process

def read_results_text(path):
    preds, golds = [], []
    with open(path, 'r', encoding = "UTF-8") as fp:
        for line in fp:
            line = line.strip()
            pred, gold = line.split('####')
            pred = eval(pred)
            pred = lower_normalize(pred)
            gold = eval(gold)
            gold = lower_normalize(gold)
            preds.append(pred)
            golds.append(gold)
    return preds, golds

def lower_normalize(list_of_tuple):
    if len(list_of_tuple) == 0:
        return list_of_tuple
    ret = []
    for item in list_of_tuple:
        if len(item) != 2:
            print(f"len({item})!=2")
            continue
        a, s = item
        ret.append((a.lower(), s.lower()))
    return ret


def read_line_examples_from_file(data_path):
    """
    Read data from file, each line is: sent####labels
    Return List[List[word]], List[Tuple]
    """
    sents, labels = [], []
    with open(data_path, 'r', encoding='UTF-8') as fp:
        words, labels = [], []
        for line in fp:
            line = line.strip()
            if line != '':
                text, tuples = line.split('####')
                sents.append(text.strip())
                labels.append(lower_normalize(eval(tuples)))
    print(f"total examples = {len(sents)}")
    return sents, labels

def read_pred_results_text(path):
    preds = []
    with open(path, 'r', encoding = "UTF-8") as fp:
        for line in fp:
            if "####" in line:
                _, label = line.strip().split("####")
                label = parse_pred_results(label)
            else:
                label = line.strip()
            pred = eval(label)
            pred = lower_normalize(pred)
            preds.append(pred)
    return preds

def parse_pred_results(line):
    import re
    p1 = re.compile(r'[[](.*)[]]', re.S)
    res = re.findall(p1, line)
    try:
        assert len(res) <= 1
    except AssertionError:
        print(line)
    if len(res) == 0:
        print(line)
        return '[]'
    return '[' + res[0] + ']' 


def compute_f1_scores(preds, golds):
    n_tp, n_gold, n_pred = 0, 0, 0
    print(len(preds))
    print(preds)
    print(len(golds))
    for i in range(len(preds)):
        
        n_gold += len(golds[i])
        n_pred += len(preds[i])
        for t in preds[i]:
            if t in golds[i]:
                n_tp += 1
            else:
                print(t)
    print(f"number of gold spans: {n_gold}, predicted spans: {n_pred}, hit: {n_tp}")
    precision = float(n_tp) / float(n_pred) if n_pred != 0 else 0
    recall = float(n_tp) / float(n_gold) if n_gold != 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if precision != 0 or recall != 0 else 0
    scores = {'precision': precision, 'recall': recall, 'f1': f1}
    return scores

def filter_tuples(pred, text):
    ret_pred = []
    if len(pred) == 0:
        return pred
    for item in pred:
        a,s = item
        if a in text.lower():
            ret_pred.append(item)
    return ret_pred

def filter_pred_results(preds, sents):
    ret_preds = []
    for idx, pred in enumerate(preds):
        ret_preds.append(filter_tuples(pred, sents[idx]))
    return ret_preds
        

if __name__ == '__main__':
    # path = './14res-results-3.txt'
    # gold_path = './data/ASPE/14res/100_test.txt'
    # pred_path = './data/ASPE/14res/100_test_3shot_conversation_results.txt'

    # gold_path = './data/ASPE/14lap/100_test.txt'
    # pred_path = './data/ASPE/14lap/100_test_9shot_seed550_results.txt'

    gold_path = './data/ASPE/14res/100_test.txt'
    pred_path = './data/ASPE/14res/100_test_3shot_seed13_explanation_results.txt'

    sents, golds = read_line_examples_from_file(gold_path)

    preds = read_pred_results_text(pred_path)
    # preds = filter_pred_results(preds, sents)

    # preds, golds = read_results_text(path)
    print(compute_f1_scores(preds, golds))

