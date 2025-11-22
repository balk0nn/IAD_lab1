import pytest
import numpy as np
from SW_Median.Solutions.Bottleneck import sliding_median_bottleneck  # замените на ваш импорт

@pytest.fixture
def small_array():
    return np.array([-2., 1., -5., 7., 2., 0., -5., 8., 3., -4.])


k_values = [3, 4, 5]


@pytest.mark.parametrize("k", k_values)
def test_sliding_median_bottleneck(small_array, k):
    arr = small_array

    # Вызов Bottleneck-реализации
    out_bn = sliding_median_bottleneck(arr, k)

    # Ручное вычисление медианы через сортировку
    expected = []
    n = len(arr)
    for i in range(n - k + 1):
        window = np.sort(arr[i:i+k])
        if k % 2 == 1:
            median = window[k // 2]
        else:
            median = (window[k // 2 - 1] + window[k // 2]) / 2
        expected.append(median)

    # Проверка
    np.testing.assert_allclose(out_bn, expected, rtol=1e-9, atol=1e-9)