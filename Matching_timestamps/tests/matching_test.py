import pytest
import numpy as np

from Matching_timestamps.Solutions import (
    TwoPointers,
    BiSearch,
    TwoPointers_numba,
    SciPy_Tree,
)

# список всех методов с именем и функцией
methods_to_test = [
    ("numpy_linear",    TwoPointers.match_timestamps),
    ("numpy_bisearch", BiSearch.match_timestamps),
    ("numba_linear", TwoPointers_numba.match_timestamps),
    ("scipy_kdtree", SciPy_Tree.match_timestamps),
]


# маленький тестовый набор данных
@pytest.mark.parametrize("method_name,func", methods_to_test)
def test_small_array(method_name, func):
    t1 = np.array([0.0, 0.091, 0.5])
    t2 = np.array([0.001, 0.09, 0.12, 0.6])

    matching = func(t1, t2)

    # ожидаемые индексы ближайших элементов
    expected = np.array([0, 1, 3], dtype=np.uint32)

    # сравниваем результат
    assert np.array_equal(matching, expected), f"{method_name} failed"


@pytest.mark.parametrize("method_name,func", methods_to_test)
def test_random_array_consistency(method_name, func):
    np.random.seed(42)
    t1 = np.sort(np.random.rand(10))
    t2 = np.sort(np.random.rand(15))

    matching = func(t1, t2)

    # проверяем, что индексы в допустимом диапазоне
    assert matching.dtype == np.uint32
    assert matching.min() >= 0
    assert matching.max() < len(t2)

    # проверяем, что действительно ближайшие элементы
    for i, idx in enumerate(matching):
        dist = abs(t1[i] - t2[idx])
        if idx > 0:
            assert dist <= abs(t1[i] - t2[idx - 1])
        if idx < len(t2) - 1:
            assert dist <= abs(t1[i] - t2[idx + 1])