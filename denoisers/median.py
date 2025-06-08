import cv2
import numpy as np

def denoise(image: np.ndarray, ksize: int = 3) -> np.ndarray:
    """Применяет медианный фильтр к каждому каналу (для цветных изображений)."""
    if image.ndim == 2:
        return cv2.medianBlur((image * 255).astype(np.uint8), ksize) / 255.0
    else:
        channels = []
        for i in range(image.shape[2]):
            ch = cv2.medianBlur((image[:, :, i] * 255).astype(np.uint8), ksize)
            channels.append(ch.astype(np.float32) / 255.0)
        return np.stack(channels, axis=2)
