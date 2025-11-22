import numpy as np


def match_timestamps(t1: np.ndarray, t2: np.ndarray) -> np.ndarray:
    """
    Timestamp matching function. It returns such array `matching` of length len(timestamps1),
    that for each index i of timestamps1 the element matching[i] contains
    the index j of timestamps2, so that the difference between
    timestamps2[j] and timestamps1[i] is minimal.
    Example:
        timestamps1 = [0, 0.091, 0.5]
        timestamps2 = [0.001, 0.09, 0.12, 0.6]
        => matching = [0, 1, 3]
    """

    idx = np.searchsorted(t2, t1, side='left')

    n2 = len(t2)
    best = np.empty(len(t1), dtype=np.uint32)

    for i in range(len(t1)):
        j = idx[i]
        cands = []

        if j < n2:
            cands.append(j)
        if j > 0:
            cands.append(j - 1)

        best[i] = min(cands, key=lambda k: abs(t2[k] - t1[i]))

    return best
