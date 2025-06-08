"""
Инструменты для работы с изображениями
"""

import os
import cv2
import numpy as np
from typing import Tuple

def load_image(path: str, grayscale: bool = False) -> np.ndarray:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR)
    return img.astype(np.float32) / 255.0  # Нормализация в диапазон [0,1]

def save_image(path: str, image: np.ndarray):
    image_uint8 = (np.clip(image, 0, 1) * 255).astype(np.uint8)
    cv2.imwrite(path, image_uint8)

def list_images(directory: str, extensions: Tuple[str] = ('.png', '.jpg', '.jpeg')) -> list:
    return [os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.lower().endswith(extensions)]
