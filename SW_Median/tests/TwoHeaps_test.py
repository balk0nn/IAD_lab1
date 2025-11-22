# test_heap_median.py
import numpy as np
import pytest
from SW_Median.Solutions.TwoHeaps import medianSlidingWindowHeaps 

@pytest.fixture
def small_array():
    return [2, -1, 5, -7, 2, 0, 5, -8, 3, 4]

@pytest.mark.parametrize("k", [3, 4, 5])
def test_median_heaps(small_array, k):
    arr = small_array

    # Вызов вашей реализации на кучах
    out_heap = medianSlidingWindowHeaps(arr, k)

    # Ручное вычисление медианы через сортировку
    expected = []
    n = len(arr)
    for i in range(n - k + 1):
        window = sorted(arr[i:i+k])
        if k % 2 == 1:
            median = window[k // 2]
        else:
            median = (window[k // 2 - 1] + window[k // 2]) / 2
        expected.append(median)

    # Проверка
    np.testing.assert_allclose(out_heap, expected, rtol=1e-9, atol=1e-9)