import cv2
resim = cv2.imread('IMG_20210616_202539.jpg')
print('yükseklik = %i   genişlik = %i   kanal sayısı = %i' %(image.shape[0],image.shape[1],image.shape[2]))
# resmin üzerine yazı yazalım
font = cv2.FONT_HERSHEY_SIMPLEX # font tipi
org = (300, 300) # yazının içinde bulunduğu dikdörtgenin sol alt köşesi
fontScale = 7 # font büyüklüğü
color = (0, 0, 0) # BGR sırasında yazının renk kodu
thickness = 12 # yazının kalınlığı
yaziliResim = cv2.putText(resim, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
# resmi yeniden boyulandır, dosyaya kaydet ve ekranda görüntüle
s = 0.2 # scale - ölçek
dim = (int(s*image.shape[1]), int(s*image.shape[0])) # boyut
yeniYaziliResim = cv2.resize(yaziliResim, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('Gumushane.jpg', yeniYaziliResim, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("Resized image with text", yeniYaziliResim)
cv2.waitKey(0)
