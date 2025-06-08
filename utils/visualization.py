import os
import matplotlib.pyplot as plt
import numpy as np
from utils.io import load_image, save_image

def visualize_comparison(original_path: str, noisy_path: str, denoised_path: str,
                         out_path: str, title: str = ""):
    orig = load_image(original_path)
    noisy = load_image(noisy_path)
    denoised = load_image(denoised_path)

    diff = np.abs(orig - denoised)

    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    axs[0].imshow(orig[..., ::-1])  # BGR → RGB
    axs[0].set_title("Оригинал")
    
    axs[1].imshow(noisy[..., ::-1])
    axs[1].set_title("С шумом")

    axs[2].imshow(denoised[..., ::-1])
    axs[2].set_title("После фильтрации")

    axs[3].imshow(diff[..., ::-1])
    axs[3].set_title("Разница")

    for ax in axs:
        ax.axis("off")

    fig.suptitle(title)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()