import os
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "results/metrics.csv"
output_dir = "results/plots"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(csv_path)

# Группировка по методу и уровню шума
for metric in ["PSNR", "SSIM"]:
    plt.figure(figsize=(10, 6))
    for method in df["method"].unique():
        data = df[df["method"] == method]
        
        # Выделим уровень шума (например, 25 из "gaussian_25")
        def extract_level(n):
            parts = n.split("_")
            return float(parts[1]) if len(parts) > 1 else 0.0

        data = data.copy()
        data["level"] = data["noise_type"].apply(extract_level)
        grouped = data.groupby("level")[metric].mean().sort_index()

        plt.plot(grouped.index, grouped.values, marker="o", label=method)

    plt.title(f"{metric} по уровням шума")
    plt.xlabel("Уровень шума")
    plt.ylabel(metric)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{metric.lower()}_by_noise_level.png"))
    plt.close()

print("Графики сохранены в:", output_dir)