import cv2
import matplotlib.pyplot as plt

img=cv2.imread('./images/einstein.jpeg',0)

last_3bits=img & 0xE0 # 11100000
diff_img=img-last_3bits

plt.figure(figsize=(10,8))
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img,cmap='gray')

plt.subplot(222)
plt.title('3 Bit Slice Image')
plt.imshow(last_3bits,cmap='gray')

plt.subplot(2,2,(3,4))
plt.title('Difference Image')
plt.imshow(diff_img,cmap='gray')

plt.tight_layout()
plt.show()
