import cv2 
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('./images/img4.jpg',0)
[m, n]=img.shape
print('Image Shape:',m,n)

f=2
for k in range(8):
    resized_img=np.zeros((m//f,n//f))
    for i in range(0,m,f):
        for j in range(0,n,f):
           resized_img[i//f][j//f]=img[i][j]
    
    plt.subplot(2,4,k+1)
    plt.title(f'({m//f}x{n//f})')
    plt.imshow(resized_img,cmap='gray')
    
    f=f*2

plt.tight_layout()
plt.show()
