# YENİ BAŞLAYANLAR İÇİN PYTHON ile OPENCV
Buradaki projelerimizde Python 3.9.6 ve OpenCV 4.5.3 kullanıyoruz. Bilgisayarınıza Python yüklemek için aşağıdaki resime tıkladığınızda açılan videoyu takip edebilirsiniz.</br>
[![IMAGE ALT TEXT HERE](figure/install-python.jpg)](https://youtu.be/QmLXzB3N5pM)</br>
Bilgisayarınıza OpenCV yüklemek için de aşağıdaki resimlere tıklandığında görüntülenen videoları sırasıyla izleyebilirsiniz.</br>
[![IMAGE ALT TEXT HERE](figure/opencv-python-resized.jpg)](https://youtu.be/aavhf3C9SlE)</br>
[![IMAGE ALT TEXT HERE](figure/Gumushane_dusuk_boyut.jpg)](https://youtu.be/-OiJgg3pnYI)</br>
Bilgisayarlarınıza Python ve OpenCV kurduktan sonra Jupyter Notebook'un içine sanal ortam (virtual environment - venv) olan opencv-env ismini kayıt etmek için aşağıdaki resme tıklayınca açılna videoyu izleyin. Bu videoda ayrıca Jupyter Notebook kullanarak bir *ipynb* kodunu da bilgisayarımızda koşturmuş olacağız.
## Proje 1: Resim Yükleme, Üzerine Yazı Yazma, Yeniden Boyutlandırma ve Kaydetme
Yani imread, putText, resize ve imwrite fonksiyonlarını kullanacağız.

*imread_puttext_resize_imwrite.py*
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
## Proje 2: Bir Resimi BGR Uzayından Gri Tonlu Hale Dönüştürüp Değişik Eşik Metodlarıyla Binary Hale Getirme

## Proje 3: Web Kamera Akışının Açılıp Videonun üzerine FPS değerinin Yazılması ve Yüz Tanıma

### Video
Kodu koşturdukran sonra elde ettiğimiz yeniden boyutlandırılmış resim aşağıda olup üzerine tıklarsanız ilgili videoyu da izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/Gumushane_dusuk_boyut.jpg)](https://www.youtube.com/watch?v=-OiJgg3pnYI)
