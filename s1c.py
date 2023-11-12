import cv2
import matplotlib.pyplot as plt
import numpy as np

def histogram_gen(image):
    histogram=np.zeros(256,dtype=int)
    for row in image:
        for pixel in row:
            histogram[pixel]+=1
    return histogram

img=cv2.imread('./images/img4.jpg',0)

histogram=histogram_gen(img)

threshold=128
segmented_img=(img>threshold).astype(np.uint8)*255

plt.figure(figsize=(9,7))
plt.subplot(2,2,(1,2))
plt.bar(range(256),histogram)
plt.title('Histogram:')

plt.subplot(2,2,3)
plt.imshow(img,cmap='gray')
plt.title('Original Image')

plt.subplot(2,2,4)
plt.imshow(segmented_img,cmap='gray')
plt.title(f'Binary Threshold: {threshold}')

plt.tight_layout()
plt.show()
