import numpy as np


def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """
    Cosine similarity between two vectors.

    u, v: shape (d,).

    Return (u . v) / (||u|| * ||v||). If either vector is all zeros (norm
    0), return 0.0 instead of dividing by zero.
    """
    if np.linalg.norm(u)==0 or np.linalg.norm(v)==0:
        return 0.0
    return u@v/(np.linalg.norm(u)*np.linalg.norm(v))
    # TODO: check both norms before dividing, not just their product.
