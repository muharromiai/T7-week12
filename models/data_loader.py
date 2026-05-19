# Nama  : Muharromi Ali Ilham
# NIM   : F1D02410082
# Kelas : C

import csv
import os

def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader if row]
    return header, rows

def get_dataset_path():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "Dataset", "medical_insurance_cost_dataset.csv")

def unique_values(rows, col_index):
    return sorted(set(row[col_index] for row in rows))

def filter_rows(rows, filters):
    result = rows
    for col_index, value in filters.items():
        if value and value != "Semua":
            result = [r for r in result if r[col_index] == value]
    return result

def compute_summary(rows, header):
    if not rows:
        return {}

    col = {name: i for i, name in enumerate(header)}

    ages = [float(r[col["age"]]) for r in rows]
    bmis = [float(r[col["bmi"]]) for r in rows]
    costs = [float(r[col["annual_medical_cost_usd"]]) for r in rows]
    incomes = [float(r[col["annual_income_usd"]]) for r in rows]

    smoker_count = sum(1 for r in rows if r[col["smoker"]] == "Yes")
    return {
        "Jumlah Data": len(rows),
        "Rata-rata Usia": f"{sum(ages) / len(ages):.1f}",
        "Rata-rata BMI": f"{sum(bmis) / len(bmis):.1f}",
        "Rata-rata Biaya Medis (USD)": f"{sum(costs) / len(costs):,.2f}",
        "Total Biaya Medis (USD)": f"{sum(costs):,.2f}",
        "Rata-rata Pendapatan (USD)": f"{sum(incomes) / len(incomes):,.2f}",
        "Jumlah Perokok": f"{smoker_count} ({smoker_count / len(rows) * 100:.1f}%)",
    }