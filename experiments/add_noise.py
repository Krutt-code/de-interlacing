"""
Добавление изображений с шумами
"""

import os
from utils.io import load_image, save_image, list_images
from utils.noise import add_gaussian_noise, add_salt_and_pepper_noise

ORIGINAL_DIR = "data/original"
OUTPUT_ROOT = "data/noisy"

# Параметры шумов
gaussian_sigmas = [10, 25, 50]
sp_amounts = [0.01, 0.03, 0.05]

images = list_images(ORIGINAL_DIR)

for path in images:
    filename = os.path.basename(path)
    image = load_image(path)

    # Гауссов шум
    for sigma in gaussian_sigmas:
        noisy = add_gaussian_noise(image, sigma=sigma)
        out_dir = os.path.join(OUTPUT_ROOT, f"gaussian_{sigma}")
        os.makedirs(out_dir, exist_ok=True)
        save_image(os.path.join(out_dir, filename), noisy)

    # Импульсный шум
    for amount in sp_amounts:
        noisy = add_salt_and_pepper_noise(image, amount=amount)
        out_dir = os.path.join(OUTPUT_ROOT, f"sp_{amount}")
        os.makedirs(out_dir, exist_ok=True)
        save_image(os.path.join(out_dir, filename), noisy)

print("Все изображения зашумлены и сохранены.")
