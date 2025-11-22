import numpy as np
import bottleneck as bn


def sliding_median_bottleneck(nums: np.ndarray, k: int):

    # bn.move_median возвращает массив той же длины, с NaN на первых (window‑1) позициях
    med = bn.move_median(nums, window=k)

    return med[k - 1:]