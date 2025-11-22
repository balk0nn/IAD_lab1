import csv
import random
import time
from tqdm import tqdm

from SW_Median.Solutions import Heaps_numba_numpy, Bottleneck, TwoHeaps, SortedList

# Список функций, которые будут сравниваться
functions_to_test = [
    ("sortedList", SortedList.medianSlidingWindow),
    ("heaps", TwoHeaps.medianSlidingWindowHeaps),
    ("heaps+numbpy", Heaps_numba_numpy.median_sliding_window),
    ("Bottleneck", Bottleneck.sliding_median_bottleneck),
]


def benchmark(func, nums, k):
    start = time.perf_counter()
    _ = list(func(nums, k))
    return time.perf_counter() - start


# ------------------------------------------------------------
# 3. ГЕНЕРАЦИЯ ОДНОГО БОЛЬШОГО МАССИВА
# ------------------------------------------------------------
def prepare_array(max_n, seed=123):
    random.seed(seed)
    return [random.randint(0, 10**6) for _ in tqdm(range(max_n))]


k_fixed = 2500
n_values = [i for i in range(10**5, int(1.1*10**6), 10**5)]
max_n = max(n_values)

base = prepare_array(max_n)

# ------------------------------------------------------------
# Сохранение результатов в CSV
# ------------------------------------------------------------

csv_filename = "results.csv"

with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["func", "n", "k", "time_sec"])   # header

    for name, func in functions_to_test:
        for n in tqdm(n_values, desc=name):
            t = benchmark(func, base[:n], k_fixed)
            writer.writerow([name, n, k_fixed, t])

print(f"\nРезультаты сохранены в {csv_filename}")
