import os
from tqdm import tqdm
from utils.io import load_image, save_image, list_images
from denoisers import median, gaussian, nl_means

# Пути
noisy_root = "data/noisy"
original_filenames = [f for f in os.listdir("data/original") if f.endswith((".png", ".jpg", ".jpeg"))]
methods = {
    "median":   median.denoise,
    "gaussian": gaussian.denoise,
    "nl_means": nl_means.denoise
}

# Перебор по типам шума
for noise_type in sorted(os.listdir(noisy_root)):
    noisy_dir = os.path.join(noisy_root, noise_type)
    if not os.path.isdir(noisy_dir):
        continue

    print(f"- Обработка шума: {noise_type}")

    images = list_images(noisy_dir)

    for method_name, method_func in methods.items():
        print(f"  -> Метод: {method_name}")
        output_dir = os.path.join("results", method_name, noise_type)
        os.makedirs(output_dir, exist_ok=True)

        for img_path in tqdm(images, desc=f"{method_name} on {noise_type}"):
            filename = os.path.basename(img_path)
            output_path = os.path.join(output_dir, filename)

            if os.path.exists(output_path):
                continue  # Пропускаем уже обработанные

            try:
                image = load_image(img_path)
                result = method_func(image)
                save_image(output_path, result)
            except Exception as e:
                print(f"Ошибка при обработке {filename} методом {method_name}: {e}")

print("Обработка завершена.")
