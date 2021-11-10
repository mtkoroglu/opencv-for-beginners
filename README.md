# Yeni Başlayanlar için PYTHON ile OpenCV
Merhaba arkadaşlar. Bu sayfada **OpenCV**'nin **OpenCV for Beginners** isimli resmi kursunu takip ediyor olacağız. Bu kursa 

https://opencv.org/course-opencv-for-beginners/

bağlantısından ulaşabilirsiniz. Kursa kayıt ücreti $117. Ben bu kursa  

https://www.kickstarter.com/projects/opencv/opencv-for-beginners

bağlantısından çok önce kayıt olup $57 ödemiştim. Sizin bu kursa kaydolmanız zorunlu değil.

Buradaki projelerimizde **Python 3.9.6** ve **OpenCV 4.5.3** kullanıyoruz. Aşağıda açıklamalarını/sonuçlarını gördüğünüz projelerin **py** ve **ipynb** uzantılı (bazen MATLAB ve C++ kodlarını da koyabiliriz ki MATLAB kodlarının uzantısı **m** iken C++ kodlarının uzantısı **cpp** olarak görünecektir) kodları yukarıda **project** isimli dosyada bulabilirsiniz. Bilgisayarınıza Python yüklemek için aşağıdaki resime tıkladığınızda açılan videoyu takip edebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/install-python.jpg)](https://youtu.be/QmLXzB3N5pM)

Bilgisayarınıza OpenCV yüklemek için de aşağıdaki resimlere tıklandığında görüntülenen videoları sırasıyla izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/opencv-python-resized.jpg)](https://youtu.be/aavhf3C9SlE)
[![IMAGE ALT TEXT HERE](figure/Gumushane_dusuk_boyut.jpg)](https://youtu.be/-OiJgg3pnYI)

Bilgisayarlarınıza **Python** ve **OpenCV** kurduktan sonra Jupyter Notebook'un içine sanal ortamımız (virtual environment - venv) olan **opencv-env** ismini kayıt etmek (register) için aşağıdaki resme tıklayınca açılan videoyu izleyin. Bu videoda ayrıca Jupyter Notebook kullanarak bir *ipynb* kodunu da bilgisayarımızda koşturmuş olacağız.

[![IMAGE ALT TEXT HERE](figure/thumbnailLQ.jpg)](https://youtu.be/6wFsCuEj5JY)
## Proje 1: Resim Yükleme, Resmin Üzerine Yazı Yazma, Resmi Yeniden Boyutlandırma ve Kaydetme
Bu egzersizde OpenCV kütüphanesinin **imread**, **putText**, **resize** ve **imwrite** fonksiyonlarını kullanacağız. Resim yüklemek için kullandığımız ilk fonksiyon olan **imread()** argüman olarak resim/fotoğraf ismi kabul ediyor. Yani fonksiyona *string* veri tipinde resmin uzantılı ismini giriş olarak veriyoruz. Mesela burada fotoğrafımızın ismi **IMG_20210616_202539.jpg** olduğundan **imread('IMG_20210616_202539.jpg')** şeklinde fonksiyonunu çağırdığımızda resmi bizim verdiğimiz değişkene yüklüyor. Bu arada gözden kaçırmayın, bütün fonksiyonları her zaman **cv2** anahtar kelimemizin sonuna **nokta** koyup çağırıyoruz, çünkü **cv2** kodda OpenCV kütüphanesini temsil ediyor. Zaten bu yüzden her kodumuzun başında **import cv2** diye bir komutla OpenCV'yi aktif hale getirmiş oluyoruz. Burada yazdıklarımızın kısa bir özeti: Eğer **IMG_20210616_202539.jpg** isimli bir resmi OpenCV kütüphanesi kullanarak Python ile okuyup **image** isminde bir değişkene atamak istiyorsak, o zaman aşağıdaki kodu koşturmalıyız.</br>
```
import cv2
image = cv2.imread('IMG_20210616_202539.jpg')
```

ve burada *type(image)* komutu ile yüklediğimiz resmin tipine bakacak olursak *numpy.ndarray* tipinde bir veri görüyoruz ki bu da bize OpenCV'nin resimleri hafızada tutmak/erişmek için *numpy* kütüphanesi kullandığını gösteriyor. Yüklediğimiz resmin *features* denilen özelliklerine bakmak istediğimizde 

```
dir(image)
```

komutunu yazarız. Karşımıza çıkan özelliklerden birisi de **shape** yani resmin şekli. Aşağıdaki kod resmin yüksekliğini (satır sayısı - height), genişliğini (sütun sayısı - width) ve BGR (veya RGB) kanal sayısını (channels) **print** komutuyla ekrana basıyor.

```
print('height = %i   width = %i   channels = %i' %(image.shape[0], image.shape[1], image.shape[2]))
```

Aşağıdaki videoyu izleyerek yukarıda anlatılan kodu Jupyter Notebook'da gerçekleyebilirsiniz.
[![IMAGE ALT TEXT HERE](figure/imread_puttext_resize_imwrite.jpg)](https://youtu.be/2bLhk2sV_jk)
## Proje 2: Web Kamerasına Erişim, Renkli Resmin Gri Tonlu ve Binary Hale Getirilmesi ve Görüntüye Filtre Uygulanması
Video dediğimiz şey ard arda yakalanan (capture) resimlerin ekranda görüntülenmesinden başka birşey değil. Burada **FPS** kavramı karşımıza çıkıyor. Yani **Frame per Second**, Türkçesi saniyedeki kare sayısı. Genelde bu değer standart web kameraları için 30. OpenCV kullanarak bilgisayarımızın web kamerasını aşağıdaki komutla açabiliriz.

```
cap = cv2.VideoCapture(0)
```

Burada **VideoCapture()** web kamerasına erişmek için yazılmış sınıf (class) ismi - bizim için basit haliyle bir komut. Bu komuta 0 girişini verdik çünkü bilgisayarımızda eğer bir web kamerası varsa o kameraya 0 atanmış. Eğer birden fazla kamera varsa, o zaman argüman olarak 0 değil de 1, 2, ... girebiliriz. Bu arada **VideoCapture** komutunun (aynı zamanda OpenCV kütüphanesinde **videoio** ana modülünde bir sınıf) bize döndürdüğü değişkene biz **cap** dedik. Burada **capture** kelimesinin kısaltması olan **cap** ismini uygun bulduk zira **capture** demek yakalamak demek ki web kamerası da saniyede otuz kez görüntüyü yakalayarak bize video sağlamış oluyor. OpenCV'de **VideoCapture** sınıfı bize web kamerası başarıyla açıldı mı açılmadı mı kontrol etmemiz için bir fonksiyon kullanımımıza sunuyor: **isOpened()**. Yukarıda **VideoCapture()** komutunun bize verdiği **cap** değişkeni üzerinden aşağıdaki gibi kontrol edelim.

```
if (cap.isOpened() == False):
    print('Web kamerasına erişimde sorun yaşandı!')
else:
    print('Kameranın FPS değeri %i.' %cap.get(cv2.CAP_PROP_FPS))
```

Eğer kamera yoksa veya erişimde (veya bağlantıda) bir sıkıntı yaşandıysa o zaman ekrana **Web kamerasına erişimde sorun yaşandı!** yazacağız. Aksi durumda kameradan **kare**ler (İng. **frame**) geliyor olacak ve web kamerasının **FPS** değerini ekrana basalım. Kameraya başarıyla eriştiğimizi kabul ederek devam ediyoruz. Şimdi görüntü sürekli gelmeye devam edeceğinden, sürekli koşacak bir döngü oluşturup bu döngü içine her girişte web kamerasından resmi alıp **frame** isimli bir değişkene atayalım ve ardından döngüden çıkmadan bu yakalanan renkli resimi sırasıyla ilk önce gri tonlu tek kanallı bir resme (**gray** isminde bir değişkene), sonra **eşikleme** (İng. **threholding**) ile **binary** yani siyah-beyaz bir resme (**bw** isminde bir değişkene) çevirelim [3].

```
while (cap.isOpened() == True):
    ret, frame = cap.read()
    s = 0.75 # ölçek (scale)
    dim = (int(s*frame.shape[1]), int(s*frame.shape[0]))
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (T, bw) = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)
    if ret == True:
        cv2.imshow('BGR image', frame)
        cv2.imshow('Gray Scale image', gray)
        cv2.imshow('Thresholded (Binary) image', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('BGR webcam image.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('BGR webcam image.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('BGR webcam image.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()
```

Buraya kadar olan kodu **web_cam_stream_bgr_gray_bw.py** ve **web_cam_stream_bgr_gray_bw.ipynb** isminde yukarda projeler kısmında ilgili projede bulabilirsiniz. Bu kodun açıklaması için aşağıdaki resime tıklayıp videoyu izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/web_cam_stream_bgr_gray_bw_thumbnail.jpg)](https://youtu.be/kSCDLw6Aa3E)

## Proje 3: Yüz Tespit Etme (Face Detection)

## Proje 4: numpy Kütüphanesi Kullanarak Gri Tonlu bir Resim Elde Etme
### Referanslar
[1] OpenCV 4.5.3 Dökümantasyonu - https://docs.opencv.org/4.5.3/</br>
[2] numpy Kütüphanesi ile Rasgele Sayı, Dizi ve Matris Üretme - https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
[3] OpenCV Thresholding by Adrian Rosebrock (pyimagesearch) - https://www.pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/
