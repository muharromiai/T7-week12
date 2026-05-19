# Nama  : Muharromi Ali Ilham
# NIM   : F1D02410082
# Kelas : C

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class ChartCanvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=4):
        self.fig = Figure(figsize=(width, height), dpi=100)
        self.fig.set_facecolor("#fafafa")
        super().__init__(self.fig)
        self.setParent(parent)

    def clear(self):
        self.fig.clear()

    def draw_bar_chart(self, rows, header):
        col = {name: i for i, name in enumerate(header)}
        data = {}
        for r in rows:
            region = r[col["region"]]
            cost = float(r[col["annual_medical_cost_usd"]])
            data.setdefault(region, []).append(cost)

        regions = sorted(data.keys())
        avgs = [np.mean(data[r]) for r in regions]
        colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]

        self.clear()
        ax = self.fig.add_subplot(111)
        bars = ax.bar(regions, avgs, color=colors[: len(regions)], edgecolor="white")
        ax.set_title("Rata-rata Biaya Medis per Region", fontsize=12, fontweight="bold")
        ax.set_xlabel("Region")
        ax.set_ylabel("Biaya Medis (USD)")
        for bar, val in zip(bars, avgs):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 200,
                f"${val:,.0f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )
        self.fig.tight_layout()
        self.draw()

    def draw_scatter_chart(self, rows, header):
        col = {name: i for i, name in enumerate(header)}
        ages_s, costs_s = [], []
        ages_n, costs_n = [], []
        for r in rows:
            age = float(r[col["age"]])
            cost = float(r[col["annual_medical_cost_usd"]])
            if r[col["smoker"]] == "Yes":
                ages_s.append(age)
                costs_s.append(cost)
            else:
                ages_n.append(age)
                costs_n.append(cost)

        self.clear()
        ax = self.fig.add_subplot(111)
        ax.scatter(ages_n, costs_n, alpha=0.5, s=20, label="Non-Smoker", color="#4e79a7")
        ax.scatter(ages_s, costs_s, alpha=0.5, s=20, label="Smoker", color="#e15759")
        ax.set_title("Usia vs Biaya Medis", fontsize=12, fontweight="bold")
        ax.set_xlabel("Usia")
        ax.set_ylabel("Biaya Medis (USD)")
        ax.legend()
        self.fig.tight_layout()
        self.draw()

    def draw_pie_chart(self, rows, header):
        col = {name: i for i, name in enumerate(header)}
        data = {}
        for r in rows:
            plan = r[col["insurance_plan"]]
            data[plan] = data.get(plan, 0) + 1

        labels = sorted(data.keys())
        sizes = [data[l] for l in labels]
        colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]

        self.clear()
        ax = self.fig.add_subplot(111)
        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            colors=colors[: len(labels)],
            startangle=90,
        )
        ax.set_title("Distribusi Insurance Plan", fontsize=12, fontweight="bold")
        self.fig.tight_layout()
        self.draw()

    def draw_histogram(self, rows, header):
        col = {name: i for i, name in enumerate(header)}
        bmis = [float(r[col["bmi"]]) for r in rows]

        self.clear()
        ax = self.fig.add_subplot(111)
        ax.hist(bmis, bins=20, color="#4e79a7", edgecolor="white", alpha=0.8)
        ax.set_title("Distribusi BMI", fontsize=12, fontweight="bold")
        ax.set_xlabel("BMI")
        ax.set_ylabel("Frekuensi")
        self.fig.tight_layout()
        self.draw()

    def export_to_png(self, filepath):
        self.fig.savefig(filepath, dpi=150, bbox_inches="tight")