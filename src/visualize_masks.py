import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define image path (update as needed)
image_path = r"D:\dataset\brain.v1i.coco-segmentation\train\y1_jpg.rf.57ff64ffc9ea36e90bd303261331d16b.jpg"
mask_path = image_path.replace(".jpg", "_mask.png").replace("train", "train/masks")

# Load the original image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load the mask (grayscale)
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Create an overlay (convert grayscale mask to RGB)
mask_overlay = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
mask_overlay[:, :, 0] = 255  # Red mask
mask_overlay[:, :, 1] = 0
mask_overlay[:, :, 2] = 0

# Blend image and mask
overlayed_image = cv2.addWeighted(image, 0.6, mask_overlay, 0.4, 0)

# Display the result
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap="gray")
plt.title("Generated Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(overlayed_image)
plt.title("Overlayed Image")
plt.axis("off")

plt.show()
 
