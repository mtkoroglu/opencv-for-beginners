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