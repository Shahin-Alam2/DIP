import cv2
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

def erosion(img,ses):
    kernel=np.ones((ses,ses),np.uint8)
    row,col=img.shape
    eroded_img=np.zeros_like(img)
    
    for i in range(ses//2,row-ses//2):
        for j in range(ses//2,col-ses//2):
            region=img[i-ses//2:i+ses//2+1,j-ses//2:j+ses//2+1]
            eroded_img[i,j]=np.min(region)
    return eroded_img

def dilation(img,ses):
    kernel=np.ones((ses,ses),np.uint8)
    row,col=img.shape
    dilated_img=np.zeros_like(img)
    
    for i in range(ses//2,row-ses//2):
        for j in range(ses//2,col-ses//2):
            region=img[i-ses//2:i+ses//2+1,j-ses//2:j+ses//2+1]
            dilated_img[i,j]=np.max(region)
    return dilated_img

img1=cv2.imread('./images/img2.jpg',0)
img2=cv2.imread('./images/img4.jpg',0)

ses1=15
ses2=10
eroded_img=erosion(img1,ses1)
dilated_img=dilation(img2,ses2)

plt.figure(figsize=(10,7))
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img1,cmap='gray')
plt.subplot(222)
plt.title('Eroded Image')
plt.imshow(eroded_img,cmap='gray')

plt.subplot(223)
plt.title('Original Image')
plt.imshow(img2,cmap='gray')
plt.subplot(224)
plt.title('Dilated Image')
plt.imshow(dilated_img,cmap='gray')

plt.tight_layout()
plt.show()