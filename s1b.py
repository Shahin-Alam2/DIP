import cv2
import matplotlib.pyplot as plt

img=cv2.imread('./images/img4.jpg',0)
sampled_img=[img.copy()]

plt.figure(figsize=(9,7))

plt.subplot(2,4,1)
plt.title('8 bit')
plt.imshow(img,cmap='gray')

for k in range(7):
    img//=2
    sampled_img.append(img.copy())
    
    plt.subplot(2,4,k+2)
    plt.title(f'({8-(k+1)}bit)')
    plt.imshow(sampled_img[k+1],cmap='gray')

plt.tight_layout()
plt.show()
