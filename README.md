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
Bu egzersizde OpenCV kütüphanesinden **imread()**, **putText()**, **resize()** ve **imwrite()** fonksiyonlarını kullanacağız. Resim yüklemek için kullandığımız fonksiyon olan **imread()** argüman olarak uzantısıyla beraber resim/fotoğraf ismi kabul ediyor. Yani fonksiyona *string* veri tipinde resmin uzantılı ismini giriş olarak veriyoruz. Mesela burada fotoğrafımızın ismi **IMG_20210616_202539.jpg** olduğundan **imread('IMG_20210616_202539.jpg')** şeklinde fonksiyonu çağırdığımızda resmi bizim ismini verdiğimiz değişkene yüklüyor. Bu arada gözden kaçırmayın, bütün fonksiyonları her zaman **cv2** anahtar kelimemizin sonuna **nokta** koyup çağırıyoruz, çünkü **cv2** kodda OpenCV kütüphanesini temsil ediyor. Zaten bu yüzden her kodumuzun başında **import cv2** diye bir komutla OpenCV'yi aktif hale getirmiş oluyoruz. Burada yazdıklarımızın kısa bir özeti: Eğer **IMG_20210616_202539.jpg** isimli bir resmi OpenCV'de Python ile okuyup **resim** isminde bir değişkene atamak istiyorsak, o zaman aşağıdaki kodu koşturmalıyız.

```
import cv2
resim = cv2.imread('IMG_20210616_202539.jpg')
```

ve burada **type(resim)** komutu ile yüklediğimiz resmin tipine bakacak olursak **numpy.ndarray** tipinde bir veri görüyoruz ki bu da bize OpenCV'nin resimleri hafızada tutmak/erişmek için **numpy** paketini kullandığını gösteriyor. Aşağıda dördüncü egzersizde **numpy** kütüphanesi kullanarak kendimiz gri tonun bütün piksel şiddet değerlerini oluşturan sentetik bir resim oluşturacağız. Bu yüzden **numpy** kütüphanesini neden kullandığımız ve de **numpy.ndarray** yani uzun haliyle **n dimendional array** (n boyutlu dizi) ne manaya geliyor, bunlar bizim için önemli. 

Yüklediğimiz resmin **features** denilen özelliklerine bakmak istediğimizde konsola

```
dir(resim)
```

komutunu yazabiliriz. Karşımıza çıkan özelliklerden birisi de **shape** yani resmin şekli (bu bizim **çok sık** kullanacağımız bir özellik - **FİNAL SINAVINDA KARŞIMIZA ÇIKACAK**). Aşağıdaki kod resmin **yüksekliğini** (height), **genişliğini** (width) ve BGR (Blue-Green-Red yani Mavi-Yeşil-Kırmızı) kanal sayısını (channels) **print** komutuyla ekrana basıyor. Burada yükseklik satır sayısına, genişlik sütun sayısına eşit. Aşağıdaki kod satırında **resim.shape[0]** ve **resim.shape[1]** komutları sırasıyla resmin yükseklik ve genişliğini piksel cinsinden bir sayı olarak ekrana basıyor. **FİNAL SINAVINDA ÇIKACAK** 

```
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(resim.shape[0], resim.shape[1], resim.shape[2]))
```

Aşağıdaki videoyu izleyerek yukarıda bir kısmı açıklanan ve tamamı aşağıda verilen kodu **Jupyter Notebook**'da gerçekleyebilirsiniz.
[![IMAGE ALT TEXT HERE](figure/imread_puttext_resize_imwrite.jpg)](https://youtu.be/2bLhk2sV_jk)

```
import cv2 # OpenCV kütüphanesine erişim
resim = cv2.imread('IMG_20210616_202539.jpg') # resim yükle
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(resim.shape[0],resim.shape[1],resim.shape[2]))
# resmin üzerine yazı yazalım
font = cv2.FONT_HERSHEY_SIMPLEX # font tipi
org = (300, 300) # yazının içinde bulunduğu dikdörtgenin sol alt köşesi
fontScale = 7 # font büyüklüğü
color = (0, 0, 0) # BGR sırasında yazının renk kodu
thickness = 12 # yazının kalınlığı
yaziliResim = cv2.putText(resim, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
# resmi yeniden boyutlandır, dosyaya kaydet ve ekranda görüntüle
s = 0.2 # scale - ölçek
dim = (int(s*resim.shape[1]), int(s*resim.shape[0])) # boyut
yeniYaziliResim = cv2.resize(yaziliResim, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('Gumushane.jpg', yeniYaziliResim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("Uzerine yazi yazilmis ve yeniden boyutlandirilmis resim", yeniYaziliResim)
cv2.waitKey(0) # klavyede herhangi bir tuşa basana kadar ekranda görüntüle
```

## Proje 2: Web Kamerasına Erişim, Renkli Resmin Gri Tonlu ve Siyah-Beyaz (Binary) Hale Dönüşümü ve Görüntüye Filtre Uygulanması
Video dediğimiz şey ard arda yakalanan (capture) resimlerin ekranda seri halde görüntülenmesinden başka birşey değil. Burada **FPS** kavramı karşımıza çıkıyor. Yani **Frame per Second**, Türkçesi saniyedeki kare sayısı. Genelde bu değer standart web kameraları için 30. OpenCV kullanarak bilgisayarımızın web kamerasını aşağıdaki komutla açabiliriz.

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

Eğer kamera yoksa veya erişimde (veya bağlantıda) bir sıkıntı yaşandıysa o zaman ekrana **Web kamerasına erişimde sorun yaşandı!** yazılacak. Aksi durumda kameradan **kare**ler (İng. **frame**) sürekli geliyor olacak ve web kamerasının **FPS** değerini ekrana basacağız. Kameraya başarıyla eriştiğimizi kabul ederek devam ediyoruz. Şimdi görüntü sürekli gelmeye devam edeceğinden, web kamerası görüntü verdiği müddetçe aktif olacak bir döngü oluşturup, bu döngü içine her girişte web kamerasından resmi alıp **frame** isimli bir değişkene atayalım ve ardından döngüden çıkmadan bu yakalanan renkli resmi sırasıyla ilk önce gri tonlu tek kanallı bir resme (**gray** isminde bir değişkene), sonra **eşikleme** (İng. **threholding**) ile **binary** yani siyah-beyaz bir resme (**bw** isminde bir değişkene) çevirelim [3].

```
while (cap.isOpened() == True):
    ret, frame = cap.read()
    s = 0.75 # ölçek (scale)
    dim = (int(s*frame.shape[1]), int(s*frame.shape[0]))
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (T, bw) = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)
    if ret == True:
        cv2.imshow('renkli resim', frame)
        cv2.imshow('gri tonlu resim', gray)
        cv2.imshow('siyah beyaz resim', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('renkli resim.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('gri tonlu resim.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('siyaz beyaz resim.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()
```

Buraya kadar olan kodu **web_cam_stream_bgr_gray_bw.py** ismiyle yukarda projeler kısmında ilgili projede bulabilirsiniz. Bu kodun açıklaması için aşağıdaki resime tıklayıp videoyu izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/web_cam_stream_bgr_gray_bw_thumbnail.jpg)](https://youtu.be/kSCDLw6Aa3E)
### OpenCV fonksiyonlarının hız bakımından "optimal" olması
Yukarıda OpenCV'nin **threshold** fonksiyonunu kullanarak gri tonlu hale getirdiğimiz **gray** isimli görüntüyü siyah beyaz hale (**bw** isminde) getirmiştik. OpenCV görüntüyü hangi veri tipi olarak bilgisayarın hafızasında tutuyor, piksellerin şiddet değerleri nedir ve bu değerlere nasıl erişilir gibi konuları anlamak ve de kendi yazdığımız bir fonksiyonu OpenCV'nin aynı işi yapan bir fonksiyonu ile hız (optimallik) açısından kıyaslamak için kendimiz **threshold()** isminde bir fonksiyon yazdık. Bu fonksiyonu **cv2.threshold()** diye değil de direk olarak **threshold()** şeklinde çağıracağız.

```
def threshold(img, T):
    bwUser = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j] > T):
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
bw = threshold(gray, 60)
```

Sonrasında kodu koşturduğumuzda ekranda duraklamalar gördük. Bu yavaşlamanın sebebi bizim yazdığımız **threshold()** fonksiyonun OpenCV'nin kendi built-in **threshold()** fonksiyonu kadar hızlı çalış(a)mamasıdır. İlgili kodun ismi **web_cam_stream_bgr_gray_user_bw.py**. Videoyu izlemek için aşağıdaki resme tıklayınız.

[![IMAGE ALT TEXT HERE](figure/user_defined_built_in.jpg)](https://youtu.be/euN1WgKzFiY)

### Gürültüyü gidermek için görüntüye filtre uygulanması
Yukarıda siyah-beyaz resme baktığımızda bazı piksellerin siyah ile beyaz arasında değiştiğini (titreme gibi) görmüştük. Gürültüyü yok etmek için resmi biraz bulandırabiliriz [4]. Bunun için de OpenCV kütüphanesinin **imgproc** isimli ana modülünden **blur()** ve **GaussianBlur()** fonksiyonlarını kullanacağız. Bu modüle bakmışken **medianBlur()** fonksiyonuyla medyan filtresine de bakalım. Ayrıca snapshot gibi bazı uygulamalarda kullanılan özel bir Gaussian bulanıklaştırma filtresi olan **bilateralFilter()** komutuna da bakacağız.

```
import cv2
cap = cv2.VideoCapture(0)
if (not cap.isOpened()):
    print('Web kamerasına erişimde sorun yaşandı!')
else:
    print('Kameranın FPS değeri %i.' %cap.get(cv2.CAP_PROP_FPS))

while (cap.isOpened() == True):
    ret, frame = cap.read()
    s = 0.75 # ölçek (scale)
    dim = (int(s*frame.shape[1]), int(s*frame.shape[0]))
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    filtered = cv2.blur(frame, (7, 7))
    # filtered = cv2.GaussianBlur(frame, (17, 17), 0)
    # filtered = cv2.medianBlur(frame, 11)
    # filtered = cv2.bilateralFilter(frame, 11, 69, 39)
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
    (T, bw) = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    if ret == True:
        cv2.imshow('renkli resim', frame)
        cv2.imshow('filtrelenmis resim', filtered)
        cv2.imshow('gri tonlu resim', gray)
        cv2.imshow('siyah beyaz resim', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('renkli.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('filtrelenmiş.jpg', filtered, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('gri tonlu.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('siyah beyaz.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı!')
        break
        
cap.release()
cv2.destroyAllWindows()
```

Yukarıdaki kodun açıklamasını izlemek için aşağıdaki resme tıklayın. Adrian Rosebrock tarafından hazırlanmış ilgili tutorial'ı okumak için [4] nolu kaynağa bakınız.

[![IMAGE ALT TEXT HERE](figure/filtering.png)](https://youtu.be/Q0SO2F0b8Hg)
## Proje 3: Yüz Tespit Etme (Face Detection)
OpenCV'de **Haar cascade** metodu ile yüz tespiti yapacağız [5]. Adrian ayrıca **Haar Cascade** kullanarak yüz tespiti yaptığı bir projede işin içerisine iki tane servo motorda koyarak mekatronik bir proje yapmış [6]. İsteyenler OpenCV'nin **Haar Cascade** tutorial'ına da göz atabilirler [7]. Yazdığımız kodun tamamı aşağıda.

```
import cv2
# OpenCV tarafından hazır olarak bize sağlanan Haar Cascade yüz tanıma metodunu yükle
print("[BİLGİ] Haar cascade yüz tanıma metodunu yüklüyor...")
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1) # web kamerasına erişim
if (not cap.isOpened()):
    print('Web kamerasına erişimde sorun yaşandı!')
count = 0 # resimleri kaydederken isimlerini sırayla artan şekilde yapmak için kullanacağımız index
while (cap.isOpened() == True):
    ret, frame = cap.read() # web kamerasından görüntüyü al
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # renkli uzaydan gri tonlu uzaya geç
    # yakalanan kare üzerinde yüz tespiti yap. rects değişkeni tespit edilen yüzü içine alan dikdörtgenin 
    # sol üst (x, y) ve sağ alt (x+w, y+h) noktalarının koordinat bilgileri. Bu bilgiler yüzü dikdörtgen 
    # içine almamız için yeterli. Burada w harfi width yani yatay genişlik, h ise height yani yükseklik.
    rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, 
    minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # yüzü rectangle() komutuyla dikdörtgen içine al
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if ret == True:
        cv2.imshow('yuz tanima', frame)
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
OpenCV'de **imread()** fonksiyonu ile *jpg* veya *png* formatında bir görüntü yüklediğimizde veya **cap = cv2.VideoCapture(0)** komutu ile web kamerasına erişip oradan kare (İng. frame) yakaladığımızda **imshow()** komutu ile monitörde **renkli** bir resim/video gördük. Bu renkli görüntünün **üç kanal**dan oluştuğunu, OpenCV'nin bu kanallara sırasıyla **B-G-R** dediğini ve açık halinin **Blue-Green-Red** yani **Mavi-Yeşil-Kırmızı** olduğunu söyledik. Her piksel üç ayrı kanal için 0-255 arası bir şiddet (İng. intensity) değerine sahip. Gri tonlu uzaya geçerken bu üç kanalın ağırlıklı ortalaması alınıyor ve tek kanala düşüyor. Yeni oluşan bu tek kanallı resime gri tonlu (İng. gray scale) resim dedik. Artık her bir piksel üç değil tek bir şiddet değerine sahip. Üç kanallı (renkli) resimdekine benzer bir mantıkla gri tonlu resimde de piksel şiddet değeri 0-255 arası bir değer alıyor. Burada **0** tam sayısı **siyah** renge, **255** de **beyaz** renge tekabül ederken ara değerler grinin tonlarını oluşturuyor. Mesela **127** değeri tam olarak **gri** renk. Yani %50 siyah - %50 beyaz karışımı olan gri. 

Bu egzersizde ilk önce **numpy** kütüphanesini aktif hale getirelim ve 256 sütuna sahip (satır sayısı değişken olabilir) bütün elemanları sıfır olan bir matris oluşturalım. Oluşturduğumuz matrisin veri tipi **uint8** olmalı çünkü gri tonlu bir görüntünün her bir pikseli bilgisayarın hafızasında **sekiz bit** yani **bir byte** yer kaplıyor. Aşağıda yazdığımız kodu görebilirsiniz. 

```
import cv2
import numpy as np
r, c = 256, 256 # satır ve sütun sayısı
resim = np.zeros((r, c), np.uint8) # r satır c sütundan oluşan elemanları sıfır olan bir matris
for i in range(resim.shape[0]): # satırları dolaşıyoruz
    for j in range(resim.shape[1]): # sütunları dolaşıyoruz
        resim[i][j] = j # i. satır j. sütundaki piksel değerini sütun numarası olan j yapalım
cv2.imshow('gri tonlu resim', resim)
cv2.imwrite('gri tonlu resim.jpg', resim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.waitKey(0)
```

Kodu koşturduğumuzda aşağıdaki sentetik görüntüyü elde ettik. Resmin ilk sütunundaki piksellerin şiddet değeri 0 olduğundan en sol taraf siyah renkle başlıyor. Sağa doğru gittikçe 0'dan 255'e kadar olan değerleri bir bir tarıyoruz. Böylece geçişlerle beyaz renge kadar gidiyoruz.

<img src="figure/gri_tonlu_resim.jpg" alt="gri tonlu resim" height="256"/>

İlgili videoyu izlemek için aşağıdaki resime tıklayın.

[![IMAGE ALT TEXT HERE](figure/BGR_to_gray_LQ.jpg)](https://youtu.be/eMBuYXLO4KI)
## ARA SINAV
Ara sınav sorularının çözümleri DBS'de dokuzuncu hafta bölümünde yapıldı. Videoları oradan izleyebilirsiniz. Ara sınavda kod içeren soruların çözümleri aşağıda. İlgili kodlar yukarıda **project/midterm** dizinine konuldu. İsteyenler kodları aşağıda da görebilir.
### Soru 5
Aşağıdaki kod ne yapmaktadır?

```
import cv2
picture = cv2.imread('abc.jpg')
print(picture.shape[0])
print(picture.shape[1])
picture = cv2.resize(picture, (int(picture.shape[1]/2), int(picture.shape[0]/2)),
interpolation = cv2.INTER_AREA)
cv2.imshow('resim', picture)
cv2.waitKey(0)
```

Bu kod ilk önce OpenCV'nin **imread()** fonksiyonu ile dosyada yer alan **abc.jpg** isimli resim dosyasını bilgisayarımızın RAM'ine okumaktadır. Yüklenen görüntüye *picture* isimli değişken ile erişebiliriz. Sonrasında **print()** komutlarıyla konsol ekranına ilk önce görüntünün piksel cinsinden yüksekliği (satır sayısı), ardından genişliği (sütun sayısı) basılıyor. Ardından gelen **resize()** komutuyla resmin eni ve boyu tam yarısına düşürülüyor. Son olarak da yeniden boyutlandırılmış resim **imshow()** komutuyla ekranda görüntüleniyor. Son satır olan **cv2.waitKey(0)** komutunda argümanın sıfır verilmesi kullanıcı tarafından bir tuşa basıldığında ekrandan görüntülenen resmin kapatılması manasına geliyor. Eğer **cv2.waitKey(2000)** deseydik görüntü ekranda 2000ms yani 2s kalıp otomatik olarak kapanacaktı. Bu şekilde otomatik olarak görüntüyü kapatma seri halinde resimleri ardarda görüntülemek istediğimiz zamanlarda oldukça kullanışlı olabilir.
### Soru 8
Aşağıdaki kodun çıktısı nedir?

```
import cv2
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
resim = cv2.imread('messi ve ronaldo.jpg')
griResim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
rects = detector.detectMultiScale(griResim, scaleFactor=1.25, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
k = 0 # tespit edilen yüz sayısı
isim = ['Ronaldo', 'Messi'] # oyuncuların isimlerini dikdörtgenin sol üst köşesinden x ekseninde kaydır
isimKaydirX = [85, 60]
for (x, y, w, h) in rects: # tespit edilen yüzleri dikdörtgen içine al ve oyuncunun ismini yazdır
    cv2.rectangle(resim, (x, y), (x + w, y + h), (255, 255, 255), 2)
    resim = cv2.putText(resim, isim[k], (x-isimKaydirX[k], y+int(h/4)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 1, cv2.LINE_AA)
    k = k + 1 # tespit edilen yüz varsa artır
yazi0 = 'Resimde %i tane yuz tespit edildi' %k
resim = cv2.putText(resim, yazi0, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 1, cv2.LINE_AA)
yazi1 = 'Yukseklik = %i piksel' %resim.shape[0]
yazi2 = 'Genislik = %i piksel' %resim.shape[1]
resim = cv2.putText(resim,yazi1,(550, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 1, cv2.LINE_AA)
resim = cv2.putText(resim,yazi2,(550, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 1, cv2.LINE_AA)
cv2.imshow('yuz tespiti', resim)
cv2.waitKey(0) # kullanıcı bir tuşa basana kadar ekranda görüntüle
```

Yukarıdaki kodu koşturduğumuzda elde ettiğimiz görüntü aşağıdaki gibidir.

<img src="figure/ronaldo and messi annotated.jpg" alt="ronaldo ve messi" height="532"/>

### Soru 10
Aşağıdaki kod koştuğunda dosyaya kaydedilen resim hangisidir? Eğer x = 100 değil de 50 olursa ne fark olacağını açıklayınız.

```
import cv2
import numpy as np
r, c = 256, 256 # resmin satır ve sütun sayısı
resim = np.zeros((r, c), np.uint8) # r satır c sütundan oluşan siyah bir resim oluştur
# resim üzerinde dolaşmaya başlıyoruz
for i in range(resim.shape[0]): # i satır numarası index’i, satırları dolaşıyoruz
    for j in range(resim.shape[1]): # j sütun numarası index’i, sütunları dolaşıyoruz
        resim[i][j] = i # resmin i. satır j. sütunundaki pikseli i yap 
x = 100 # quality kelimesi kalite manasına gelir
cv2.imwrite('resim.jpg', resim, [cv2.IMWRITE_JPEG_QUALITY, x])
```

Yukarıdaki kodu koşturduğumuzda aşağıdaki gibi bir resim elde ederiz. Eğer x=100 değilde x=50 seçilirse dosyaya kaydedilen *resim.jpg* dosyasının boyutu (kilobyte veya megabyte cinsinden) daha az olur ve kaydedilen resim görüntülendiğinde daha kötü (piksel piksel) gözükür. Burada resmin boyutu küçülür diyenlerden kısmi puan kırıldı çünkü resmin boyutu denilince akla gelen ilk kavram resmin satır ve sütun sayısı (resmin piksel cinsinden boyu ve eni).

<img src="figure/gray_scale_midterm.jpg" alt="gri tonlu resim" height="256"/>

### Soru 11
Ara sınavda sorulan sorunun cevabı olan kod aşağıda.

```
import cv2
resim = cv2.imread('giraffe.jpg', cv2.IMREAD_COLOR)
##################### resmi değişik filtrelerden geçir ############################
k = 25
fresim1 = cv2.blur(resim, [k, k])
fresim2 = cv2.GaussianBlur(resim, [k, k], 0)
fresim3 = cv2.medianBlur(resim, k)
fresim4 = cv2.bilateralFilter(resim, 49, 85, 95)
########## ekranda görüntüleyebilmek için resmi yeniden boyutlandır ###############
s = 1/6
dim = (int(s*resim.shape[1]), int(s*resim.shape[0]))
resim0 = cv2.resize(resim, dim, cv2.INTER_LINEAR)
resim1 = cv2.resize(fresim1, dim, cv2.INTER_LINEAR)
resim2 = cv2.resize(fresim2, dim, cv2.INTER_LINEAR)
resim3 = cv2.resize(fresim3, dim, cv2.INTER_LINEAR)
resim4 = cv2.resize(fresim4, dim, cv2.INTER_LINEAR)
####################### resimleri ekranda görüntüle ###############################
cv2.imshow('original', resim0)
cv2.imshow('cv2.blur()', resim1)
cv2.imshow('cv2.GaussianBlur()', resim2)
cv2.imshow('cv2.medianBlur()', resim3)
cv2.imshow('cv2.bilateralFilter()', resim4)
cv2.waitKey(0) # kullanıcı klavyeden herhangi bir tuşa basana kadar bekle
########################## resimleri dosyaya yaz ###################################
cv2.imwrite('giraffe blur.jpg', fresim1, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe GaussianBlur.jpg', fresim2, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe medianBlur.jpg', fresim3, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe bilateralFilter.jpg', fresim4, [cv2.IMWRITE_JPEG_QUALITY, 100])
```

Yukarıdaki koda **numpy** kütüphanesi kullanarak birleştirilmiş resim oluşturmayı ekleyelim. Genişletilmiş resmi oluşturmak için ilk önce genişletilmiş resim boyutunda boş bir matris oluşturduk. 

```
# orijinal, GaussianBlur() ve bilateralFilter() resim sonuçlarını tek resim haline getir
r, c = resim.shape[0], resim.shape[1]
resimBirlesik = np.zeros((r, 3*c, 3), np.uint8)
```

Burada **resimBirlesik** isimli matris üç boyutlu çünkü genişletilmiş resmi BGR yani renkli resimlerden oluşturuyoruz. Satır sayısı bir resim ile aynı olmakla beraber sütun sayısı bir resmin üç katı. Ardından **slicing** denilen metodla boş matrisin ilgili **1/3**'lük paylarına tekabül eden resimleri koyuyoruz.

```
resimBirlesik[0:r, 0:c, :] = resim
resimBirlesik[0:r, c:2*c, :] = fresim2
resimBirlesik[0:r, 2*c:3*c, :] = fresim4
```

Resmin üzerine yazı yazmaya önceden çok baktık. İlgili kodda **cv2.putText()** komutlarını bulup inceleyebilirsiniz. Aşağıdaki resmi çıktı veren genişletilmiş koda yukarıda **project/midterm** dizininin içerisinde **question11_extended.py** ismiyle erişebilirsiniz.

<img src="figure/giraffe_birlesik_resim_resized.jpg" alt="gri tonlu resim" height="400"/>

### Soru 13
Aşağıdaki kod ne yapmaktadır?

```
import cv2
cap = cv2.VideoCapture(0) # cap kelimesi capture manasında yakalamak demek
while(True):
    ret, kare = cap.read() 
    cv2.imshow('frame', kare)
    if cv2.waitKey(1) & 0xFF == ord('q'): # kullanıcı q tuşuna basarsa
        cv2.imwrite('resim.jpg', kare, [cv2.IMWRITE_JPEG_QUALITY, 100])
        break
cap.release()
cv2.destroyAllWindows()
```

Yukarıdaki program bilgisayarımızda web kamerasına erişip videoyu oluşturan kareleri yakalayıp ekranda ard arda görüntülemektedir. Kullanıcı bir anlık bile olsa klavyeden 'q' tuşuna basarsa, o anda görüntülenmekte olan kareyi dosyaya *resim.jpg* ismiyle bir resim olarak kaydetmekte ve koşmakta olan programı sonlandırmaktadır.
## PROJE 5: Stereo Web Kamerası Akışından Genişletilmiş Resim oluşturma
Final sınavına yönelik bir egzersiz olduğundan bu koda vakit ayıracağız. Aşağıdaki kodu yukarıda **project/stereo** dosyasının içinde **imwrite_webcam_stereo_image.py** ismiyle bulabilirsiniz.

```
import cv2
import numpy as np
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
while(True):
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    r, c = frame0.shape[0], frame0.shape[1]
    frameStereo = np.zeros((r, 2*c, 3), np.uint8)
    frameStereo[:,0:c,:] = frame0
    frameStereo[:,c:2*c,:] = frame1
    cv2.imshow('webcam stereo image', frameStereo)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        cv2.imwrite('webcam_stereo_image.jpg', frameStereo, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('Resim başarıyla kaydedildi.')
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap0.release()
cap1.release()
cv2.destroyAllWindows()
```

Genişletilmiş koda yukarıda **project/stereo** dizininde **imwrite_webcam_stereo_image_extended.py** isimli dosyadan erişebilirsiniz. Genişletilmiş kodda iki ayrı web kamerası tarafından yakalanan karelerin yüksekliklerinin farklı olma durumu göz önüne alınıyor ve kare numarası (İng. *frame number*) birleştirilmiş resmin sağ üst köşesine yazdırılıyor. Genişletilmiş kod koşarken klavyeden **r** tuşuna (**record** yani kayıt demek) basılarak alınan örnek iki resim aşağıda gösterilmiştir.

<img src="figure/webcam_stereo_image_0.jpg" alt="birleştirilmiş resim" height="240"/>
<img src="figure/webcam_stereo_image_1.jpg" alt="birleştirilmiş resim" height="240"/>

## PROJE 6: HSV Renk Uzayından Faydalanarak Yeşil Top Tespiti (Dizüstü Bilgisayar'da ve Raspberry Pi'da)
Bugüne kadar gri tonlu (İng. gray scale) ve RGB diye adlandırılan Red-Green-Blue yani Kırmızı-Yeşil-Mavi renk uzaylarında çalıştık. RGB renk uzayında renk oluşturmayı anlamak için bu uzayı aşağıda *Şekil 1*'de gösterildiği gibi bir kübe benzeteceğiz.

<img src="https://929687.smushcdn.com/2407837/wp-content/uploads/2021/04/opencv_color_spaces_rgb_cube.png?lossy=1&strip=1&webp=1" alt="RGB cube" height="300"/>

*Şekil 1*: RGB renk uzayını temsil eden küp ([8]'in izni ile). Renk oluştururken kanal değerleri [0-255] arasında değişebilir. OpenCV'de kanal sıralamasının RGB değil de BGR olduğu göz önüne alınırsa mavi = (255, 0, 0), yeşil = (0, 255, 0) ve kırmızı = (0, 0, 255) olarak kodlanır. Şekle bakarak sarı rengin (0, 255, 255) olarak kodlandığını kendiniz çıkarabilirsiniz. Final sınavında bu şekil verilerek majenta ve turkuaz (cyan) renklerinin kodları sorulabilir. Ara sınavda RGB uzayında siyah, beya ve gri renk kodları sorulmuştu, final sınavında yine bu bilgilere ihtiyaç duyulabilir.

RGB uzayı her ne kadar renkli bir uzay olsa da görüntü işleme alanında çalışan uzmanlar renge göre nesne tespiti/takibi yapacakları (yani görüntüyü bir sinyal olarak kabul edecek olursak bu sinyaldeki renk **özelliğine**<sup>1</sup> bakacakları) zaman daha uygun/kolay olduğundan dolayı renk tanımlarını RGB uzayında değil de HSV uzayı denilen başka bir renk uzayında yapıyorlar [8]. HSV uzayı RGB uzayı gibi kartezyen bir koordinat sisteminde değil de *Şekil 2*'de görüldüğü gibi silindirik bir koordinat sisteminde temsil ediliyor.

<img src="https://929687.smushcdn.com/2407837/wp-content/uploads/2021/04/opencv_color_spaces_hsv_cylinder.png?lossy=1&strip=1&webp=1" alt="HSV color space" height="360"/>
*Şekil 2*: HSV renk uzayı.

Web kamerasındandan gelen görüntüleri ard arda yakalamaya başladığımız sonsuz döngüye girince her kareyi gürültüden arındırmak için ilk önce Gaussian bulanıklaştırma filtresinden geçiriyoruz.

```
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
```

Ardından renk tespitinde kolaylık sağlayalım diye B-G-R uzayından H-S-V uzayına geçiyoruz.

```
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
```

Sonrasında yazdığımız kodun (yukarıda **project/ball_tracking** isimli dizinde **ball_tracking.py** isimli dosya) baş taraflarında

```
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
```

değişkenleri ile H-S-V uzayında aralığı tanımlanan yeşil nesneleri

```
mask = cv2.inRange(hsv, greenLower, greenUpper)
```

komutuyla tespit ediyoruz. Aşağıdaki resimde web kamerasından yakalanan resim (a) şıkkında, **inRange()** komutu tespit edilen yeşil bölgeli resim (b) şıkkında gösterilmiştir (yeşil bölge beyaz, kalan bölge siyah). Dikkat edilirse (b)'deki resimde topun olduğu bölgenin dışında az ve küçük de olsa başka bölgeler de mevcuttur. Tespit etmeyi arzu etmediğimiz bu bölgelerden kurtulmak için **cv2.erode()** isimli fonksiyonu (aşağıdaki kodda altı kere kendini tekrar edecek biçimde) koşturuyoruz 

```
mask = cv2.erode(mask, None, iterations=6)
```

ve (c) şıkkında verilen erozyona uğramış resmi elde ediyoruz. Bunu takip eden kodumuzda **cv2.dilate()** komutunu da benzer bir şekilde (sekiz kere tekrar edecek şekilde) koşturunca 

```
mask = cv2.dilate(mask, None, iterations=8)
```

(d) şıkkında verilen son resmi elde ediyoruz. Burada **morphology** denilen **erode** ve **dilate** işlemlerini uygulayarak yeşil alanı daha iyi tespit etmiş olduk.

<img src="figure/morphology.png" alt="captured image, green region, erosion and dilation" height="480"/>

Şimdi **findContours()** isimli fonksiyonla resimde tespit ettiğimiz bölgelere sınırlar çizdirip, ardından bu sınırlardan en büyük olanını seçip bu kontura bir çember (circle) çizdiriyoruz. Bu şekilde tespit ettiğimiz yeşil topu sarı renkte bir çember içinde göstermiş oluyoruz.

OpenCV'de yeşil top tespiti/takibi tutorial'ı için Adrian'ın sayfasına bakabilirsiniz [9]. Bizim derste yazdığımız kod için yukarıda **project/ball_tracking** isimli dizinde **ball_tracking.py** ve **ball_tracking_fps.py** isimli kodlara bakın. Kodun açıklaması için yukarıdaki yorumları okuyabileceğiniz gibi aşağıdaki videoyu da izleyebilirsiniz.

[![IMAGE ALT TEXT HERE](figure/top_takibi.jpg)](https://youtu.be/Htb1co2PUQM)

### PROJE 7: FPS Değerinin Hesaplanması ve Görüntülenmesi
Web kamerasından yakaladığımız son kareyi işledikten hemen sonra bir zaman etiketi (İng. time stamp) alırsak bir önceki etiketten farkını hesaplayarak işlem hızımızı ölçebiliriz. Görüntü işlemede **FPS** değeri bir nevi işlem hızımıza tekabül ediyor: FPS ne kadar büyükse o kadar hızlı, ne kadar küçükse o kadar yavaş işlem yapıyoruz demektir. İşlem hızımız donanımımıza bağlı olduğu gibi (e.g., nvidia ekran kartı, bilgisayarın CPU'su, Raspberry Pi) koşan algoritmanın basitliğine/kompleksliğine de direk bağlıdır.



İlgili kod yukarıda **project/ball_tracking/ball_tracking_fps.py** isimli dosyada. Python'da **time** paketini kullanırken internette bir örnekten faydalandık [10].

<img src="figure/top_takibi_0.jpg" alt="HSV color space" height="240"/><img src="figure/top_takibi_1.jpg" alt="HSV color space" height="240"/>

### Dipnotlar
<sup>1</sup> İng. feature.

### Referanslar
[1] OpenCV 4.5.3 Dökümantasyonu - https://docs.opencv.org/4.5.3/</br>
[2] Standard Kütüphane ve **numpy** ile Rasgele Sayı, Dizi ve Matris Üretme - https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/</br>
[3] OpenCV'de Eşikleme (Thresholding) [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/</br>
[4] OpenCV'de Görüntü Filtreleme (Bulandırma) [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/</br>
[5] OpenCV'de **Haar Cascade** Metodu ile Yüz Tespiti [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2021/04/05/opencv-face-detection-with-haar-cascades/</br>
[6] Raspberry Pi ve OpenCV kullanarak Pan-Tilt Kamera ile Yüz Takibi [A. Rosebrock, pyimagesearch.com] - https://www.pyimagesearch.com/2019/04/01/pan-tilt-face-tracking-with-a-raspberry-pi-and-opencv/</br>
[7] Haar Cascade ile Yüz ve Göz Tespiti (OpenCV tutorial) - https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html</br>
[8] OpenCV'de Renk Uzayları Arasında Dönüşüm - https://www.pyimagesearch.com/2021/04/28/opencv-color-spaces-cv2-cvtcolor/</br>
[9] OpenCV ile Yeşil Top Tespiti (Takibi) - https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/</br>
[10] OpenCV'de **time** paketi kullanılarak FPS hesaplanması - https://www.geeksforgeeks.org/python-displaying-real-time-fps-at-which-webcam-video-file-is-processed-using-opencv/
