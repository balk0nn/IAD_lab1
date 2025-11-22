import numpy as np
from numba import njit


@njit
def median_sliding_window(nums, k):
    n = len(nums)
    if k > n or k <= 0:
        return np.empty(0, dtype=np.float64)

    out = np.empty(n - k + 1, dtype=np.float64)
    window = np.empty(k, dtype=np.float64)

    # Инициализация первого окна
    for i in range(k):
        window[i] = nums[i]
    window.sort()

    # Получаем медиану
    if k % 2 == 1:
        out[0] = window[k // 2]
    else:
        out[0] = 0.5 * (window[k // 2 - 1] + window[k // 2])

    for i in range(k, n):
        old_val = nums[i - k]
        new_val = nums[i]

        # Удаляем старое значение через поиск
        idx = np.searchsorted(window, old_val)
        # Сдвигаем элементы влево
        for j in range(idx, k - 1):
            window[j] = window[j + 1]

        # Вставляем новое значение через поиск
        insert_idx = np.searchsorted(window[:k - 1], new_val)
        for j in range(k - 1, insert_idx, -1):
            window[j] = window[j - 1]
        window[insert_idx] = new_val

        # Берём медиану
        if k % 2 == 1:
            out[i - k + 1] = window[k // 2]
        else:
            out[i - k + 1] = 0.5 * (window[k // 2 - 1] + window[k // 2])

    return out