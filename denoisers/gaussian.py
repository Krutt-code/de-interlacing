import cv2
import numpy as np

def denoise(image: np.ndarray, ksize: int = 5, sigma: float = 1.0) -> np.ndarray:
    """Применяет гауссов фильтр к каждому каналу."""
    if image.ndim == 2:
        return cv2.GaussianBlur(image, (ksize, ksize), sigma)
    else:
        return cv2.GaussianBlur(image, (ksize, ksize), sigma)
