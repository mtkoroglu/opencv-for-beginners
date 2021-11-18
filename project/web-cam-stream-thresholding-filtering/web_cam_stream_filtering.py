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