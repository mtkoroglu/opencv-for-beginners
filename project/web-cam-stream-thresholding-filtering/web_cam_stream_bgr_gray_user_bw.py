import cv2
import numpy as np

def threshold(img, T):
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
    # (T, bw) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    bw = threshold(gray, 60)
    if ret == True:
        cv2.imshow('renkli resim', frame)
        cv2.imshow('gri tonlu resim', gray)
        cv2.imshow('siyah beyaz resim', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('renkli resim.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('gri tonlu resim.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite('siyah beyaz resim.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    else:
        print('Kare yakalanamadı!')
        break
cap.release()
cv2.destroyAllWindows()