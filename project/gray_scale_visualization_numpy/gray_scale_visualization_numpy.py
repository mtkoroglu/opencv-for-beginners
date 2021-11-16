import cv2
import numpy as np
r, c = 256, 256
resim = np.zeros((r, c), np.uint8)
# resim üzerinde dolaşmaya başlıyoruz
for i in range(resim.shape[0]): # satırları dolaşıyoruz
    for j in range(resim.shape[1]): # sütunları dolaşıyoruz
        resim[i][j] = j
cv2.imwrite('gri tonlu resim.jpg', resim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow('resim', resim)
cv2.waitKey(0)