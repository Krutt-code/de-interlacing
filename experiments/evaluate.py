import os
import csv
from utils.io import load_image
from metrics.psnr import compute_psnr
from metrics.ssim import compute_ssim

methods = ["median", "gaussian", "nl_means"]
noise_types = sorted(os.listdir("data/noisy"))
original_dir = "data/original"
results_dir = "results"
output_csv = "results/metrics.csv"

# Подготовка CSV
with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["method", "noise_type", "filename", "PSNR", "SSIM"])

    for method in methods:
        for noise_type in noise_types:
            denoised_dir = os.path.join(results_dir, method, noise_type)
            noisy_images = sorted(os.listdir(denoised_dir))

            for filename in noisy_images:
                orig_path = os.path.join(original_dir, filename)
                denoised_path = os.path.join(denoised_dir, filename)

                if not os.path.exists(orig_path) or not os.path.exists(denoised_path):
                    continue

                try:
                    orig = load_image(orig_path)
                    denoised = load_image(denoised_path)

                    psnr = compute_psnr(orig, denoised)
                    ssim = compute_ssim(orig, denoised)

                    writer.writerow([method, noise_type, filename, f"{psnr:.4f}", f"{ssim:.4f}"])
                except Exception as e:
                    print(f"! Ошибка для {filename} ({method}/{noise_type}): {e}")

print("Метрики сохранены в:", output_csv)