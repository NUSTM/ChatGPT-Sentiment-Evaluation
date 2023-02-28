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
    ret = []
    for a,s in list_of_tuple:
        ret.append((a.lower(), s.lower()))
    return ret


def compute_f1_scores(preds, golds):
    n_tp, n_gold, n_pred = 0, 0, 0
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


if __name__ == '__main__':
    path = './14res-results-3.txt'
    preds, golds = read_results_text(path)
    print(compute_f1_scores(preds, golds))

