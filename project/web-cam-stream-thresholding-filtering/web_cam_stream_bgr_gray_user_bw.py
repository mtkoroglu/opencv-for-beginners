import cv2
import numpy as np

def gray_to_bw(img, T):
    bwUser = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i][j] <= T):
                bwUser[i][j] = 0
            else:
                bwUser[i][j] = 255
    return bwUser

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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #(T, bw) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    bw = gray_to_bw(gray, 60)
    if ret == True:
        cv2.imshow('BGR image', frame)
        cv2.imshow('Gray Scale image', gray)
        cv2.imshow('Thresholded (Binary) image', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('BGR webcam image.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('gray scale webcam image.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('thresholded webcam image.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()