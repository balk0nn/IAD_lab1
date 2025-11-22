import csv
import plotext as plt
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
        t = float(row["time_sec"])
        data[name].append(t)

# ------------------------------------------------------------
# Построение графика в консоль
# ------------------------------------------------------------
plt.clear_data()
plt.clear_figure()
plt.theme('dark')
plt.title("Matching Timestamps Benchmark")
plt.xlabel("test index")
plt.ylabel("time (seconds)")

for name, values in data.items():
    xs = list(range(1, len(values)+1))
    ys = values
    plt.plot(xs, ys, label=name, marker='dot')

plt.show()
