import cv2
# Haar cascade yüz tespiti metodunu yükle
print("[BİLGİ] Haar Cascade yüz tespiti metodunu yüklüyor...")
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)
if (not cap.isOpened()):
    print('Web kamerasına erişimde sorun yaşandı!')
count = 0
while (cap.isOpened() == True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # yüz tanımayı gerçekleştir
    rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, 
    minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # tespit edilen yüzü resmin üzerinde dikdörtgen şeklinde çizdir
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if ret == True:
        cv2.imshow('face detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            imageName = 'face_detection_%i.jpg' %count
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