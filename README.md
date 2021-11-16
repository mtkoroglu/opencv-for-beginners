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

Bilgisayarlarınıza **Python** ve **OpenCV** kurduktan sonra **Jupyter Notebook**'un içine sanal ortamımız (virtual environment - venv) olan **opencv-env** ismini kayıt etmek (register) için aşağıdaki resme tıklayınca açılan videoyu izleyin. Bu videoda ayrıca **Jupyter Notebook** kullanarak bir **ipynb** kodunu da bilgisayarımızda koşturmuş olacağız. Dosyanın uzantısının açık hali **interactive python notebook**, kısa haliyle **ipynb**.

[![IMAGE ALT TEXT HERE](figure/thumbnailLQ.jpg)](https://youtu.be/6wFsCuEj5JY)
## Proje 1: Resim Yükleme, Resmin Üzerine Yazı Yazma, Resmi Yeniden Boyutlandırma ve Kaydetme
Bu egzersizde OpenCV kütüphanesinden **imread**, **putText**, **resize** ve **imwrite** fonksiyonlarını kullanacağız. Resim yüklemek için kullandığımız ilk fonksiyon olan **imread()** argüman olarak resim/fotoğraf ismi kabul ediyor. Yani fonksiyona *string* veri tipinde resmin uzantılı ismini giriş olarak veriyoruz. Mesela burada fotoğrafımızın ismi **IMG_20210616_202539.jpg** olduğundan **imread('IMG_20210616_202539.jpg')** şeklinde fonksiyonunu çağırdığımızda resmi bizim verdiğimiz değişkene yüklüyor. Bu arada gözden kaçırmayın, bütün fonksiyonları her zaman **cv2** anahtar kelimemizin sonuna **nokta** koyup çağırıyoruz, çünkü **cv2** kodda OpenCV kütüphanesini temsil ediyor. Zaten bu yüzden her kodumuzun başında **import cv2** diye bir komutla OpenCV'yi aktif hale getirmiş oluyoruz. Burada yazdıklarımızın kısa bir özeti: Eğer **IMG_20210616_202539.jpg** isimli bir resmi OpenCV kütüphanesi kullanarak Python ile okuyup **image** isminde bir değişkene atamak istiyorsak, o zaman aşağıdaki kodu koşturmalıyız.

```
import cv2
image = cv2.imread('IMG_20210616_202539.jpg')
```

ve burada **type(image)** komutu ile yüklediğimiz resmin tipine bakacak olursak **numpy.ndarray** tipinde bir veri görüyoruz ki bu da bize OpenCV'nin resimleri hafızada tutmak/erişmek için **numpy** kütüphanesi kullandığını gösteriyor. Aşağıda dördüncü egzersizde **numpy** kütüphanesi kullanarak kendimiz gri tonun bütün piksel şiddet değerlerini tarayan bir resim oluşturacağız, bu yüzden **numpy** kütüphanesini neden kullandığımızı ve de **numpy.ndarray** yani uzun haliyle **n dimedional array** ne demek anlamak biizm için birazcık önemli. 

Yüklediğimiz resmin **features** denilen özelliklerine bakmak istediğimizde 

```
dir(image)
```

komutunu yazarız. Karşımıza çıkan özelliklerden birisi de **shape** yani resmin şekli (bu bizim çok sık kullanacağımız bir özellik). Aşağıdaki kod resmin yüksekliğini (satır sayısı - height), genişliğini (sütun sayısı - width) ve BGR (veya RGB) kanal sayısını (channels) **print** komutuyla ekrana basıyor.

```
print('height = %i   width = %i   channels = %i' %(image.shape[0], image.shape[1], image.shape[2]))
```

Aşağıdaki videoyu izleyerek yukarıda anlatılan kodu **Jupyter Notebook**'da gerçekleyebilirsiniz.
[![IMAGE ALT TEXT HERE](figure/imread_puttext_resize_imwrite.jpg)](https://youtu.be/2bLhk2sV_jk)
## Proje 2: Web Kamerasına Erişim, Renkli Resmin Gri Tonlu ve Binary Hale Getirilmesi ve Görüntüye Filtre Uygulanması
Video dediğimiz şey ard arda yakalanan (capture) resimlerin ekranda görüntülenmesinden başka birşey değil. Burada **FPS** kavramı karşımıza çıkıyor. Yani **Frame per Second**, Türkçesi saniyedeki kare sayısı. Genelde bu değer standart web kameraları için 30. OpenCV kullanarak bilgisayarımızın web kamerasını aşağıdaki komutla açabiliriz.

```
cap = cv2.VideoCapture(0)
```

Burada **VideoCapture()** web kamerasına erişmek için yazılmış sınıf (class) ismi - bizim için bir komut. Bu komuta 0 girişini verdik çünkü bilgisayarımızda eğer bir web kamerası varsa o kameraya 0 atanmış. Eğer birden fazla kamera varsa, o zaman argüman olarak 0 değil de 1, 2, ... girebiliriz. Bu arada **VideoCapture** komutunun (aynı zamanda OpenCV kütüphanesinde **videoio** ana modülünde bir sınıf) bize döndürdüğü değişkene biz **cap** dedik. Burada **capture** kelimesinin kısaltması olan **cap** ismini uygun bulduk zira **capture** demek yakalamak demek ki web kamerası da saniyede otuz kez görüntüyü yakalayarak bize video sağlamış oluyor. OpenCV'de **VideoCapture** sınıfı bize web kamerası başarıyla açıldı mı açılmadı mı kontrol etmemiz için bir fonksiyon kullanımımıza sunuyor: **isOpened()**. Yukarıda **VideoCapture()** komutunun bize döndürdüğü **cap** değişkeni üzerinden aşağıdaki gibi kontrol edelim.

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

### OpenCV fonksiyonlarının hız bakımından "optimal" olması
Yukarıda OpenCV'nin **threshold** fonksiyonunu kullanarak gri tonlu hale getirdiğimiz **gray** isimli görüntüyü siyah beyaz hale (**bw** isminde) getirmiştik. OpenCV görüntüyü hangi veri tipi olarak bilgisayarın hafızasında tutuyor, piksellerin şiddet değerleri nedir ve bu değerlere nasıl erişilir gibi konuları anlamak ve de kendi yazdığımız bir fonksiyonu OpenCV'nin aynı işi yapan bir fonksiyonu ile hız (optimallik) açısından kıyaslamak için koda aşağıda verilen **gray_to_bw()** fonksiyonunu ekledik. Bu fonksiyon OpenCV'deki **threshold()** fonksiyonu ile aynı işi yapsın.

```
def gray_to_bw(img, T):
    bwUser = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j] <= T):
                bwUser[i][j] = 0
            else:
                bwUser[i][j] = 255
    return bwUser
```

Yukarıda gri tonlu görüntüyle aynı boyutta (satır ve sütun sayısı aynı olan) yeni bir resim (bütün piksel değerleri sıfır olan) oluşturabilmek için **numpy** kütüphanesinden **zeros_like()** komutunu çağırmamız gerekti. Bu yüzden de kodumuzun başına

```
import numpy as np
```

satırını ekledik. Daha önceden OpenCV yükleme videolarında sanal ortamımız **opencv-env**'a **numpy** yüklemiş olduğumuzdan bu pakete bir satırla sorunsuz erişebildik. Yoksa sanal odaya ayrıca yüklememiz gerekecekti. Bu değişikliklerin ardından ana döngümüzde ilgili yeri şöyle güncelledik.

```
# (T, bw) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
bw = gray_to_bw(gray, 60)
```

Sonrasında kodu koşturduğumuzda ekranda duraklamalar gördük. Bu yavaşlamanın sebebi bizim yazdığımız **gray_to_bw()** fonksiyonun OpenCV'nin kendi built-in **threshold()** fonksiyonu kadar hızlı çalışmamasıdır. İlgili kodun ismi **web_cam_stream_bgr_gray_user_bw.py** ve **web_cam_stream_bgr_gray_user_bw.ipynb**. Videoyu izlemek için aşağıdaki resme tıklayınız.

[![IMAGE ALT TEXT HERE](figure/user_defined_built_in.jpg)](https://youtu.be/euN1WgKzFiY)

### Gürültüyü gidermek için görüntüye filtre uygulanması
Yukarıda siyah-beyaz resme baktığımızda bazı piksellerin siyah ile beyaz arasında değiştiğini (titreme gibi) görmüştük. Gürültüyü yok etmek için resmi biraz bulandırabiliriz [4]. Bunun için de OpenCV kütüphanesinin **imgproc** isimli ana modülünden **blur()** ve **GaussianBlur()** fonksiyonlarını kullanacağız. Bu modüle bakmışken **medianBlur()** fonksiyonuyla medyan filtresine de bakalım. Ayrıca snapshot gibi bazı uygulamalarda kullanılan özel bir Gaussian bulanıklaştırma filtresi olan **bilateralFilter()** komutuna da bakacağız.

```
import cv2
cap = cv2.VideoCapture(1) # cap kelimesi capture manasında
# kamera başarıyla açıldı mı diye kontrol edelim
if (cap.isOpened() == False):
    print('Kameraya erişilemedi!')
else:
    print('FPS = %i' %cap.get(cv2.CAP_PROP_FPS))
while (cap.isOpened() == True):
    ret, frame = cap.read()
    s = 0.75 # ölçek (scale)
    dim = (int(s*frame.shape[1]), int(s*frame.shape[0]))
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    filtered = cv2.blur(frame, (7, 7))
    # filtered = cv2.GaussianBlur(frame, (7,7), 0)
    # filtered = cv2.medianBlur(frame, 7)
    # filtered = cv2.bilateralFilter(frame, 11, 61, 39)
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
    (T, bw) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    if (ret == True):
        cv2.imshow('renkli', frame)
        cv2.imshow('filtrelenmis', filtered)
        cv2.imshow('gri tonlu', gray)
        cv2.imshow('siyah beyaz', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('BGR.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('filtered.jpg', filtered, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('gray scale.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('thresholded.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı')
        break

cap.release()
cv2.destroyAllWindows()
```

Yukarıdaki kodun açıklamasını izlemek için aşağıdaki resme tıklayın. Adrian Rosebrock tarafından hazırlanmış ilgili tutorial'ı okumak için [4] nolu kaynağa bakınız.

[![IMAGE ALT TEXT HERE](figure/filtering.png)](https://youtu.be/Q0SO2F0b8Hg)
## Proje 3: Yüz Tespit Etme (Face Detection)
OpenCV'de **Haar cascade** metodu ile yüz tespiti yapacağız [5]. Adrian ayrıca **Haar Cascade** kullanarak yüz tespiti yaptığı bir projede işin içerisine iki tane servo motorda koyarak mekatronik bir proje yapmış [6]. İsteyenler OpenCV'nin **Haar Cascade** tutorial'ına da göz atabilirler. Yazdığımız kodun tamamı aşağıda.

```
import cv2
# OpenCV tarafından hazır olarak bize sağlanan Haar Cascade yüz tanıma metodunu yükle
print("[BİLGİ] Haar cascade yüz tanıma metodunu yüklüyor...")
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)
if (not cap.isOpened()):
    print('Web kamerasına erişimde sorun yaşandı!')
count = 0
while (cap.isOpened() == True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # yakalanan kare üzerinde yüz tespiti yap
    rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, 
    minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # yüzü kare içine al
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if ret == True:
        cv2.imshow('face detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            imageName = 'face detection %i.jpg' %count
            cv2.imwrite(imageName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            print('Resim %s ismiyle kaydedildi.' %imageName)
            count = count + 1
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print('Güle güle!')
            break
        else:
            continue
    else:
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()
```

[![IMAGE ALT TEXT HERE](figure/bgr_image.jpg)](https://www.youtube.com/watch?v=twqV7TOBU3s)
## Proje 4: NUMPY Kütüphanesi Kullanarak Gri Uzayın Bütün Tonlarını Tarayan Sentetik Bir Resim Oluşturma
Bildiğimiz gibi, genelde **imread()** fonksiyonu ile *jpg* veya *png* formatında bir görüntü yüklediğimizde veya **cap = cv2.VideoCapture(0)** komutu ile web kamerasına erişip oradan kare (İng. frame) yakaladığımızda **imshow()** komutu ile monitörde **renkli** bir resim/video gördük. Bu renkli görüntünün **üç kanal**dan oluştuğunu, OpenCV'nin bu kanallara sırasıyla **B-G-R** dediğini ve açık halinin **Blue-Green-Red** yani **Mavi-Yeşil-Kırmızı** olduğunu söyledik. Her piksel üç ayrı kanal için 0-255 arası bir şiddet (İng. intensity) değerine sahip. Gri tonlu uzaya geçerken bu üç kanalın ağırlıklı ortalaması alınıyor ve tek kanala düşüyor. Yeni oluşan bu tek kanallı resime gri tonlu (İng. gray scale) resim dedik. Artık her bir piksel üç değil tek bir şiddet değerine sahip. Üç kanallı (renkli) resimdekine benzer bir mantıkla gri tonlu resimde de piksel şiddet değeri 0-255 arası bir değer alıyor. Burada 0 siyah renge, 255 de beyaz renge tekabül ederken ara değerler grinin tonlarını oluşturuyor. Mesela 127 değeri tam olarak gri. Burada ilk önce **numpy** kütüphanesini aktif hale getirelim ve 256 sütuna sahip bütün elemanları sıfırdan oluşan bir matris oluşturalım. Oluşturduğumuz matrisin veri tipi **uint8** olmalı çünkü gri tonlu bir görüntünün her bir pikseli bilgisayarın hafızasında sekiz bit yani bir byte yer kaplıyor. Aşağıda yazdığımız kodu görebilirsiniz. 

```
import cv2
import numpy as np
r, c = 256, 256
resim = np.zeros((r, c), np.uint8)
for i in range(resim.shape[0]):
    for j in range(resim.shape[1]):
        resim[i][j] = j
cv2.imshow('görüntü', resim)
cv2.imwrite('gri tonlu resim.jpg', resim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.waitKey(0)
```

Kodu koşturduğumuzda aşağıdaki sentetik görüntüyü elde ettik.

<img src="figure/gri_tonlu_resim.jpg" alt="gri tonlu resim" height="256"/>

İlgili videoyu izlemek için aşağıdaki resime tıklayın.

[![IMAGE ALT TEXT HERE](figure/BGR_to_gray_LQ.jpg)](https://youtu.be/eMBuYXLO4KI)
### Referanslar
[1] OpenCV 4.5.3 Dökümantasyonu - https://docs.opencv.org/4.5.3/</br>
[2] numpy Kütüphanesi ile Rasgele Sayı, Dizi ve Matris Üretme - https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/</br>
[3] OpenCV'de Eşikleme (Thresholding) [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/</br>
[4] OpenCV'de Görüntü Filtreleme (Bulandırma) [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/</br>
[5] OpenCV'de **Haar Cascade** metodu ile Yüz Tespiti [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/05/opencv-face-detection-with-haar-cascades/</br>
[6] Raspberry Pi ve OpenCV ile Mekatronik Yüz Takibi Projesi [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2019/04/01/pan-tilt-face-tracking-with-a-raspberry-pi-and-opencv/
[7] OpenCV'nin Haar Cascade ile Yüz ve Göz Tespiti tutorial'ı - https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
