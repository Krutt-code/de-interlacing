from skimage.metrics import structural_similarity as ssim
import numpy as np

def compute_ssim(img1: np.ndarray, img2: np.ndarray) -> float:
    """Вычисляет SSIM для цветных и ч/б изображений."""
    if img1.ndim == 3 and img1.shape[2] == 3:
        return ssim(img1, img2, channel_axis=2, data_range=1.0)
    return ssim(img1, img2, data_range=1.0)