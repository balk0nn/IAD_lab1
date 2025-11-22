import csv
import time
from tqdm import tqdm
import numpy as np

from Matching_timestamps.Solutions import (
    BiSearch,
    SciPy_Tree,
    TwoPointers_numba,
    TwoPointers,
)

# Список функций, которые будут сравниваться
functions_to_test = [
    ("numpy_linear", TwoPointers.match_timestamps),
    ("numpy_bisearch", BiSearch.match_timestamps),
    ("numba_linear", TwoPointers_numba.match_timestamps),
    ("scipy_kdtree", SciPy_Tree.match_timestamps),
]


def benchmark(func, ts1, ts2):
    start = time.perf_counter()
    _ = func(ts1, ts2)
    return time.perf_counter() - start


# ------------------------------------------------------------
# 1. Генерация данных
# ------------------------------------------------------------
def make_timestamps(fps: int, st_ts: float, fn_ts: float) -> np.ndarray:
    """
    Create array of timestamps. This array is discretized with fps,
    but not evenly.
    Timestamps are assumed sorted nad unique.
    Parameters:
    - fps: int
        Average frame per second
    - st_ts: float
        First timestamp in the sequence
    - fn_ts: float
        Last timestamp in the sequence
    Returns:
        np.ndarray: synthetic timestamps
    """
    # generate uniform timestamps
    timestamps = np.linspace(st_ts, fn_ts, int((fn_ts - st_ts) * fps))
    # add an fps noise
    timestamps += np.random.randn(len(timestamps))
    timestamps = np.unique(np.sort(timestamps))
    return timestamps


if __name__ == '__main__':
    n_values = [100_000, 200_000, 400_000, 600_000, 800_000]
    fps1, fps2 = 30, 60
    st_ts = time.time()
    fn_ts = st_ts + 3600 * 2  # 2 часа

    # ------------------------------------------------------------
    # 2. Сохранение результатов в CSV
    # ------------------------------------------------------------
    csv_filename = "results_timestamps.csv"

    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["func", "n1", "n2", "time_sec"])  # header

        for name, func in functions_to_test:
            for n in tqdm(n_values, desc=name):
                ts1 = make_timestamps(fps1, st_ts, st_ts + n / fps1)
                ts2 = make_timestamps(fps2, st_ts + 200, st_ts + 200 + n / fps2)
                t = benchmark(func, ts1, ts2)
                writer.writerow([name, len(ts1), len(ts2), t])

    print(f"\nРезультаты сохранены в {csv_filename}")