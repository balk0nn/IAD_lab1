import csv
import matplotlib.pyplot as plt
from collections import defaultdict

csv_filename = "results_timestamps.csv"

# ------------------------------------------------------------
# Загрузка CSV
# ------------------------------------------------------------
data = defaultdict(list)

with open(csv_filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["func"]
        n1 = int(row["n1"])
        t = float(row["time_sec"])
        data[name].append((n1, t))


# ------------------------------------------------------------
# Построение графика
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))

for name, values in data.items():
    values.sort()  # сортируем по n1
    xs = [v[0] for v in values]
    ys = [v[1] for v in values]
    plt.plot(xs, ys, marker='o', label=name)

plt.xlabel("Number of timestamps in ts1")
plt.ylabel("Time (seconds)")
plt.title("Timestamp Matching Benchmark")
plt.grid(True)
plt.legend()
plt.show()