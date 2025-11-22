import csv
import plotext as plt
from collections import defaultdict

csv_filename = "results.csv"  # или results_timestamps.csv

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
# Построение графика в консоль
# ------------------------------------------------------------

plt.clear_data()
plt.clear_figure()
plt.title("Benchmark results")
plt.xlabel("n")
plt.ylabel("time (seconds)")

for name, values in data.items():
    values.sort()  # сортируем по n
    xs = [v[0] for v in values]
    ys = [v[1] for v in values]
    plt.plot(xs, ys, label=name, marker='dot')  # легенду задаём здесь

plt.show()