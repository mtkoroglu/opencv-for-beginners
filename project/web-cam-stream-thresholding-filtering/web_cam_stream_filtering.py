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
    # filtered = cv2.blur(frame, (7, 7))
    # filtered = cv2.GaussianBlur(frame, (17, 17), 0)
    # filtered = cv2.medianBlur(frame, 11)
    filtered = cv2.bilateralFilter(frame, 11, 69, 39)
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
    (T, bw) = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    if ret == True:
        cv2.imshow('BGR image', frame)
        cv2.imshow('filtered image', filtered)
        cv2.imshow('Gray Scale image', gray)
        cv2.imshow('Thresholded (Binary) image', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('BGR webcam image.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('filtered webcam image.jpg', filtered, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('gray scale webcam image.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('thresholded webcam image.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()