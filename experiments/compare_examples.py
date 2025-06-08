import os
from utils.visualization import visualize_comparison

# Настройки
examples = ["kodim01.png", "kodim04.png", "kodim07.png"]
noise_type = "gaussian_25"
methods = ["median", "gaussian", "nl_means"]

for method in methods:
    for filename in examples:
        orig_path = os.path.join("data/original", filename)
        noisy_path = os.path.join("data/noisy", noise_type, filename)
        denoised_path = os.path.join("results", method, noise_type, filename)

        out_path = os.path.join("results", "compare", method, noise_type, filename.replace(".png", "_comp.png"))
        title = f"{method.upper()} / {noise_type} / {filename}"

        if not all(map(os.path.exists, [orig_path, noisy_path, denoised_path])):
            print(f"! Пропущен {filename} для метода {method}")
            continue

        visualize_comparison(orig_path, noisy_path, denoised_path, out_path, title)

print("Сравнительные изображения сохранены.")