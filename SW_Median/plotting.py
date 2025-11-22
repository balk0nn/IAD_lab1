import csv
import matplotlib.pyplot as plt
from collections import defaultdict


csv_filename = "results.csv"

# ------------------------------------------------------------
# Загрузка CSV
# ------------------------------------------------------------

data = defaultdict(list)

with open(csv_filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["func"]
        n = int(row["n"])
        t = float(row["time_sec"])
        data[name].append((n, t))


# ------------------------------------------------------------
# Построение графика
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

for name, values in data.items():
    values.sort()                   # сортируем по n
    xs = [v[0] for v in values]
    ys = [v[1] for v in values]
    plt.plot(xs, ys, marker='o', label=name)

plt.xlabel("n")
plt.ylabel("time (seconds)")
plt.title("Sliding Median Benchmark (k = 2500)")
plt.grid(True)
plt.legend()
plt.show()