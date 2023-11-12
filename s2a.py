import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('./images/img4.jpg',0)

min_range=0
max_range=40

enhanced_img=img.copy()
enhanced_img[(img >= min_range)&(img <= max_range)] += 90

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title('Enhanced Image:')
plt.imshow(enhanced_img, cmap='gray')

plt.tight_layout()
plt.show()
