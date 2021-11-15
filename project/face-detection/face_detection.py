import cv2
# haar cascade yüz tanıma metodunu yükle
print("[BİLGİ] Haar cascade yüz tanıma metodunu yüklüyor...")
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)
if (not cap.isOpened()):
    print('Web kamerasına erişimde sorun yaşandı!')
i = 0
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
            imageName = 'face detection %i.jpg' %i
            cv2.imwrite(imageName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            print('Resim %s ismiyle kaydedildi.' %imageName)
            i = i + 1
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