import numpy as np


def conv1d(x: np.ndarray, kernel: np.ndarray, mode: str) -> np.ndarray:
    """
    1D cross-correlation ("convolution" in the deep-learning sense: the
    kernel is NOT flipped) with "valid" or "same" zero padding.

    x: shape (n,). kernel: shape (k,), k odd. mode: "valid" or "same".

    "valid": no padding, output length n - k + 1.
    "same": zero-pad x by k // 2 on each side first, output length n.

    Slide the kernel across the (possibly padded) signal without flipping
    it, taking sum(window * kernel) at each position.
    """
    if mode == "same":
        pad = len(kernel) // 2
        x = np.pad(x, (pad, pad), mode="constant")
    elif mode != "valid":
        raise ValueError("mode must be 'valid' or 'same'")

    n = len(x)
    k = len(kernel)
    output_length = n - k + 1
    output = np.empty(output_length, dtype=np.result_type(x, kernel))

    for i in range(output_length):
        window = x[i:i + k]
        output[i] = np.sum(window * kernel)

    return output
