# YENİ BAŞLAYANLAR İÇİN PYTHON ile OPENCV
Buradaki projelerimizde **Python 3.9.6** ve **OpenCV 4.5.3** kullanıyoruz. Aşağıda açıklamalarını/sonuçlarını gördüğünüz projelerin **py** ve **ipynb** uzantılı (bazen MATLAB ve C++ kodlarını da koyabiliriz ki MATLAB kodlarının uzantısı **m** iken C++ kodlarının uzantısı **cpp** olarak görünecektir) kodları yukarıda **project** isimli dosyada bulabilirsiniz. Bilgisayarınıza Python yüklemek için aşağıdaki resime tıkladığınızda açılan videoyu takip edebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/install-python.jpg)](https://youtu.be/QmLXzB3N5pM)

Bilgisayarınıza OpenCV yüklemek için de aşağıdaki resimlere tıklandığında görüntülenen videoları sırasıyla izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/opencv-python-resized.jpg)](https://youtu.be/aavhf3C9SlE)

[![IMAGE ALT TEXT HERE](figure/Gumushane_dusuk_boyut.jpg)](https://youtu.be/-OiJgg3pnYI)

Bilgisayarlarınıza **Python** ve **OpenCV** kurduktan sonra Jupyter Notebook'un içine sanal ortamımız (virtual environment - venv) olan **opencv-env** ismini kayıt etmek (register) için aşağıdaki resme tıklayınca açılan videoyu izleyin. Bu videoda ayrıca Jupyter Notebook kullanarak bir *ipynb* kodunu da bilgisayarımızda koşturmuş olacağız.

[![IMAGE ALT TEXT HERE](figure/thumbnailLQ.jpg)](https://youtu.be/6wFsCuEj5JY)
## Proje 1: Resim Yükleme, Resmin Üzerine Yazı Yazma, Resmi Yeniden Boyutlandırma ve Kaydetme
Bu kodda OpenCV kütüphanesinin *imread*, *putText*, *resize* ve *imwrite* fonksiyonlarını kullanacağız. Resim yüklemek için kullandığımız ilk fonksiyon olan *imread()* argüman olarak resim/fotoğraf ismi kabul ediyor. Yani fonksiyona *string* veri tipinde resmin uzantılı ismini giriş olarak veriyoruz. Mesela burada fotoğrafımızın ismi **'IMG_20210616_202539.jpg'** olduğundan *imread('IMG_20210616_202539.jpg')* şeklinde fonksiyonunu çağırırdığımızda resmi ismini bizim verdiğimiz değişkene atamış oluyor. Bu arada unutmayın her zaman bütün fonksiyonları **cv2** anahtar kelimemizin sonuna **nokta** koyup çağırıyoruz çünkü **cv2** kodda OpenCV kütüphanesinin temsil ediyor. Zaten bu yüzden her kodumuzun başında *import cv2* diye bir komutla OpenCV'yi aktif hale getimiş oluyoruz. Burada yazdığımızın özeti olarak; eğer **'IMG_20210616_202539.jpg'** isimli bir resmi OpenCV kütüphanesi kullanarak Python ile okuyup *image* isminde bir değişkene atamak istiyorsak, o zaman aşağıdaki kodu koşturmalıyız.</br>
```
import cv2
image = cv2.imread('IMG_20210616_202539.jpg')
```

ve burada *type(image)* komutu ile yüklediğimiz resmin tipine bakacak olursak *numpy.ndarray* tipinde bir veri görüyoruz ki bu da bize OpenCV'nin resimleri hafızada tutmak/erişmek için *numpy* kütüphanesi kullandığını gösteriyor. Yüklediğimiz resmin *features* denilen özelliklerine bakmak istediğimizde 

```
dir(image)
```

komutunu yazarız. Karşımıza çıkan özelliklerden birisi de *shape* yani resmin şekli. Aşağıdaki kod resmin yüksekliğini (satır sayısı), genişliğini (sütun sayısı) ve BGR (veya RGB) kanal sayısını bize verip ekrana basıyor.

```
print('height = %i   width = %i   channels = %i' %(image.shape[0],image.shape[1],image.shape[2]))
```

Aşağıdaki videoyu izleyerek yukarıda anlatılan kodu Jupyter Notebook'da gerçekleyebilirsiniz.
[![IMAGE ALT TEXT HERE](figure/imread_puttext_resize_imwrite.jpg)](https://youtu.be/6wFsCuEj5JY)
## Proje 2: Bir Resmi BGR Uzayından Gri Tonlu Hale Dönüştürüp Değişik Eşik Uygulayarak Binary Hale Getirme

## Proje 3: Web Kamera Akışının Açılıp Videonun üzerine FPS değerinin Yazılması ve Yüz Tanıma

### Referanslar
[1] OpenCV 4.5.3 Dökümantasyonu - https://docs.opencv.org/4.5.3/</br>
[2]
