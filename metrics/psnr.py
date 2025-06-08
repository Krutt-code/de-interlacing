import numpy as np

def compute_psnr(img1: np.ndarray, img2: np.ndarray) -> float:
    """Вычисляет PSNR между двумя изображениями."""
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    return 10 * np.log10(1.0 / mse)  # Для нормализованных изображений
