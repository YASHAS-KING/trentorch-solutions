import numpy as np


def causal_mask_misfire(scores: np.ndarray) -> np.ndarray:
    """
    Row-wise, numerically stable softmax under a causal mask: for query
    row i, only key columns j <= i are visible. Forbidden entries (j > i)
    must be exactly 0.0 in the output.

    scores: shape (n, n).
    """
    n = scores.shape[0]

    mask = np.triu(np.ones((n, n), dtype=bool), k=1)
    masked_scores = np.where(mask, -np.inf, scores)

    row_max = np.max(masked_scores, axis=1, keepdims=True)
    exp_scores = np.exp(masked_scores - row_max)

    probabilities = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    return probabilities
