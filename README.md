# YENİ BAŞLAYANLAR İÇİN PYTHON ile OPENCV
## Resim Yükleme, Üzerine Yazı Yazma, Yeniden Boyutlandırma ve Kaydetme
*load_superimpose_resize_write.py*
```
import cv2
image = cv2.imread('IMG_20210616_202539.jpg')
print('Resim boyutu:')
print(image.shape)
# write text on image
font = cv2.FONT_HERSHEY_SIMPLEX # font
# Bottom-left corner of the text string in the image
org = (300, 300) # (550, 300) 
fontScale = 7
color = (0, 0, 0) # BGR order
thickness = 12 # Line thickness of 2 px
imageText = cv2.putText(image, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imwrite('Gumushane.jpg', imageText, [cv2.IMWRITE_JPEG_QUALITY, 100])
# resize images and display
nOfCols = 600.0
r = nOfCols / image.shape[1]
dim = (int(nOfCols), int(image.shape[0]*r))
resizedImageText = cv2.resize(imageText, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('Gumushane_dusuk_boyut.jpg', resizedImageText, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("resized image with text", resizedImageText)
cv2.waitKey(0)
```
### Video
Kodu koşturdukran sonra elde ettiğimiz yeniden boyutlandırılmış resim aşağıda olup üzerine tıklarsanız ilgili videoyu da izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/gumushane_dusuk_boyut.jpg)](https://www.youtube.com/watch?v=-OiJgg3pnYI)
