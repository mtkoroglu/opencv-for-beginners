import cv2
import numpy as np
resim = cv2.imread('giraffe.jpg', cv2.IMREAD_COLOR)
# resimi değişik filtrelerden geçir
k = 25
filtrelenmisResim1 = cv2.blur(resim, [k, k])
filtrelenmisResim2 = cv2.GaussianBlur(resim, [k, k], 0)
filtrelenmisResim3 = cv2.medianBlur(resim, k)
filtrelenmisResim4 = cv2.bilateralFilter(resim, 49, 85, 95)
# ekranda görüntüleyebilmek için resimi yeniden boyutlandır
s = 0.28
dim = (int(s*resim.shape[1]), int(s*resim.shape[0]))
resim0 = cv2.resize(resim, dim, cv2.INTER_LINEAR)
resim1 = cv2.resize(filtrelenmisResim1, dim, cv2.INTER_LINEAR)
resim2 = cv2.resize(filtrelenmisResim2, dim, cv2.INTER_LINEAR)
resim3 = cv2.resize(filtrelenmisResim3, dim, cv2.INTER_LINEAR)
resim4 = cv2.resize(filtrelenmisResim4, dim, cv2.INTER_LINEAR)
# orijinal, GaussianBlur() ve bilateralFilter() resim sonuçlarını tek resim haline getir
r = resim.shape[0]
c = resim.shape[1]
resimBirlesik = np.zeros((r, 3*c, 3), np.uint8)
resimBirlesik[0:r, 0:c, :] = resim
resimBirlesik[0:r, c:2*c, :] = filtrelenmisResim2
resimBirlesik[0:r, 2*c:3*c, :] = filtrelenmisResim4
# birleşik resmin üzerine yazı yaz
font = cv2.FONT_HERSHEY_SIMPLEX # font tipi
fontScale = 2 # font büyüklüğü
color = (0, 0, 0) # BGR sırasında yazının renk kodu
thickness = 3 # yazının kalınlığı
resimBirlesik = cv2.putText(resimBirlesik, 'original', (c-350, 150), font, fontScale, color, thickness, cv2.LINE_AA)
resimBirlesik = cv2.putText(resimBirlesik, 'GaussianBlur()', (2*c-550, 150), font, fontScale, color, thickness, cv2.LINE_AA)
resimBirlesik = cv2.putText(resimBirlesik, 'bilateralFilter()', (3*c-560, 150), font, fontScale, color, thickness, cv2.LINE_AA)
resimBirlesik = cv2.resize(resimBirlesik, (int(s*resimBirlesik.shape[1]), int(s*resimBirlesik.shape[0])), cv2.INTER_LINEAR)
# resimleri ekranda görüntüle
cv2.imshow('original', resim0)
cv2.imshow('cv2.blur()', resim1)
cv2.imshow('cv2.GaussianBlur()', resim2)
cv2.imshow('cv2.medianBlur()', resim3)
cv2.imshow('cv2.bilateralFilter()', resim4)
cv2.imshow('birlesik resim', resimBirlesik)
cv2.waitKey(0)
# resimleri dosyaya
cv2.imwrite('giraffe GaussianBlur.jpg', filtrelenmisResim2, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe bilateralFilter.jpg', filtrelenmisResim4, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe birlesik resim resized.jpg', resimBirlesik, [cv2.IMWRITE_JPEG_QUALITY, 100])
