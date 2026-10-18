def best_f1_threshold(scores: list[float], y: list[int]) -> tuple[float, float]:
    """
    The score threshold that maximizes F1 (predict positive if score >= t).

    scores: n predicted scores. y: n true labels, each 0 or 1.

    For each distinct value in scores, using it as threshold t, compute
    F1(t) over the whole dataset. Return (best_threshold, best_f1).

    Ties for the best F1 are broken by the LARGER threshold. A threshold
    where precision or recall is undefined (a zero denominator) can never
    win. Sort once and sweep with running TP/FP counts, O(n log n), not
    a from-scratch recompute per threshold.
    """
    data = sorted(zip(scores, y), reverse=True)
    
    p_total = sum(y)
    tp = 0
    fp = 0
    
    best_f1 = -1.0
    best_threshold = float('inf')
    
    n = len(data)
    n_minus_1 = n - 1
    
    for i, (score, label) in enumerate(data):
        tp += label
        fp += 1 - label
        if i == n_minus_1 or score != data[i + 1][0]:
            if tp > 0:
                f1 = (2.0 * tp) / (tp + fp + p_total)
                if f1 > best_f1:
                    best_f1 = f1
                    best_threshold = score
                    
    return best_threshold, best_f1
