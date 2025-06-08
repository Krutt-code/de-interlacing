"""
Инструменты для добавления шумов на изображения
"""

import numpy as np
from skimage.util import random_noise

def add_gaussian_noise(image: np.ndarray, sigma: float = 25.0) -> np.ndarray:
    """Добавляет аддитивный гауссов шум с заданным q (в шкале 0–255)."""
    sigma_norm = sigma / 255.0
    noise = np.random.normal(0, sigma_norm, image.shape)
    noisy = image + noise
    return np.clip(noisy, 0.0, 1.0)

def add_salt_and_pepper_noise(image: np.ndarray, amount: float = 0.01) -> np.ndarray:
    """Добавляет импульсный шум (соль и перец) с заданной плотностью."""
    noisy = random_noise(image, mode='s&p', amount=amount)
    return np.clip(noisy, 0.0, 1.0)
