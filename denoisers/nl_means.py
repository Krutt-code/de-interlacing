import cv2
import numpy as np

def denoise(image: np.ndarray, h: float = 10.0, templateWindowSize: int = 7, searchWindowSize: int = 21) -> np.ndarray:
    """Применяет Non-Local Means к каждому каналу."""
    if image.ndim == 2:
        noisy_uint8 = (image * 255).astype(np.uint8)
        result = cv2.fastNlMeansDenoising(noisy_uint8, None, h, templateWindowSize, searchWindowSize)
        return result.astype(np.float32) / 255.0
    else:
        noisy_uint8 = (image * 255).astype(np.uint8)
        result = cv2.fastNlMeansDenoisingColored(noisy_uint8, None, h, h, templateWindowSize, searchWindowSize)
        return result.astype(np.float32) / 255.0
