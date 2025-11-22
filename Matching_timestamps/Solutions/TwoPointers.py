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

    n1 = len(t1)
    n2 = len(t2)

    matching = np.empty(n1, dtype=np.uint32)

    j = 0
    for i in range(n1):
        x = t1[i]

        while j + 1 < n2 and t2[j + 1] <= x:
            j += 1

        if j + 1 < n2:
            if abs(t2[j + 1] - x) < abs(t2[j] - x):
                matching[i] = j + 1
            else:
                matching[i] = j
        else:
            matching[i] = j

    return matching
