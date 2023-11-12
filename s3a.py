import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
from numpy import median

def add_noise(img):
    row,col=img.shape
    #salt noise
    number_of_pixels=random.randint(300,10000)
    for i in range(number_of_pixels):
        y_cord=random.randint(0,row-1)
        x_cord=random.randint(0,col-1)
        img[y_cord][x_cord]=255
    #pepper noise
    number_of_pixels=random.randint(300,10000)
    for i in range(number_of_pixels):
        y_cord=random.randint(0,row-1)
        x_cord=random.randint(0,col-1)
        img[y_cord][x_cord]=255
    return img

def cal_psnr(img,noisy_img):
    img=img.astype(np.float64)
    noisy_img=noisy_img.astype(np.float64)
    
    mse=np.mean((img-noisy_img)**2)
    max_pixel=255
    psnr=20*np.log10(max_pixel/np.sqrt(mse))
    return psnr

def avg_fltr(img,kernel_size):
    height,width=img.shape
    fltr_img=img.copy()
    
    padding=kernel_size//2
    mask=np.ones((kernel_size,kernel_size))/(kernel_size**2)
    
    for i in range(padding,height-padding):
        for j in range(padding,width-padding):
            neighborhood=img[i-padding:i+padding+1,j-padding:j+padding+1]
            conv_res=neighborhood*mask
            
            avg_value=np.sum(conv_res)
            fltr_img[i,j]=avg_value
    return fltr_img

def  median_fltr(img,kernel_size):
    height,width=img.shape
    fltr_img=img.copy()
    
    padding=kernel_size//2
    for i in range(padding,height-padding):
        for j in range(padding,width-padding):
            neighborhood=img[i-padding:i+padding+1,j-padding:j+padding+1]
            med_value=median(neighborhood)
            fltr_img[i,j]=med_value
    return fltr_img
    
    
img=cv2.imread('./images/img4.jpg',0)
noisy_img=img.copy()
noisy_img=add_noise(noisy_img)

psnr_noise=cal_psnr(img,noisy_img)
avg_fltr_img=avg_fltr(noisy_img,5)
psnr_avg=cal_psnr(img,avg_fltr_img)
median_fltr_img=median_fltr(noisy_img,5)
psnr_median=cal_psnr(img,median_fltr_img)

plt.figure(figsize=(10,7))
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img,cmap='gray')
plt.subplot(222)
plt.title('Noisy Image (PSNR= {:.2f} DB)'.format(psnr_noise))
plt.imshow(noisy_img,cmap='gray')
plt.subplot(223)
plt.title('Average Filter Image (PSNR={:.2f}) DB'.format(psnr_avg))
plt.imshow(avg_fltr_img,cmap='gray')
plt.subplot(224)
plt.title('Median Filter Image (PSNR={:.2f} DB)'.format(psnr_median))
plt.imshow(median_fltr_img,cmap='gray')

plt.tight_layout()
plt.show()