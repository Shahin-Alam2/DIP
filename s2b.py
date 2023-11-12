import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('./images/img4.jpg',0)
#img3=cv2.imread('./images/img2.jpg',0)
img2=img.copy()
img3=img.copy()

gamma=5
power_law=np.power(img/255.0, gamma)*255.0
power_law=power_law.astype(np.uint8)

c1=255.0/np.log10(1+img2.max())
log=c1*np.log10(1+img2)
log=log.astype(np.uint8)

c2=255.0/np.log10(1+img3.max())
inverse_log=np.power(10,(img3/c2))-1
inverse_log=inverse_log.astype(np.uint8)

plt.figure(figsize=(10,7))
plt.subplot(2,2,1)
plt.title('Original Image')
plt.imshow(img,cmap='gray')
plt.subplot(222)
plt.title('Power Law Transform (Gamma={:.2f})' .format(gamma))
plt.imshow(power_law,cmap='gray')

plt.subplot(223)
plt.title('Log Transform (c1={:.2f})'.format(c1))
plt.imshow(log,cmap='gray')
plt.subplot(224)
plt.title('Inverse Log (c2={:.2f})'.format(c2))
plt.imshow(inverse_log,cmap='gray')

plt.tight_layout()
plt.show()