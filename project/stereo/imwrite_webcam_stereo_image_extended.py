import cv2
import numpy as np
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
count = 0
frameNumber = 0
while(True):
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    if ret0 and ret1:
        frameNumber = frameNumber + 1
    if frameNumber == 1:
        r0, c0 = frame0.shape[0], frame0.shape[1]
        r1, c1 = frame1.shape[0], frame1.shape[1]
        if r0 == r1:
            continue
        elif r0 > r1: # eğer ilk resim büyükse
            s = r1/r0
            dim = (int(s*frame0.shape[1]), int(s*frame0.shape[0]))
            frame0 = cv2.resize(frame0, dim, cv2.INTER_LINEAR)
            r0, c0 = frame0.shape[0], frame0.shape[1]
        else:
            s = r0/r1
            dim = (int(s*frame1.shape[1]), int(s*frame1.shape[0]))
            frame1 = cv2.resize(frame1, dim, cv2.INTER_LINEAR)
            r1, c1 = frame1.shape[0], frame1.shape[1]
    frameStereo = np.zeros((r0, c0+c1, 3), np.uint8)
    frameStereo[:,0:c0,:] = frame0
    frameStereo[:,c0:c0+c1,:] = frame1
    frameNumberText = 'Frame #%i' %frameNumber
    font = cv2.FONT_HERSHEY_SIMPLEX # font tipi
    org = (c0+c1-250, 50) # yazının içinde bulunduğu dikdörtgenin sol alt köşesi
    fontScale = 1 # font büyüklüğü
    color = (0, 0, 0) # BGR sırasında yazının renk kodu
    thickness = 2 # yazının kalınlığı
    frameStereo = cv2.putText(frameStereo, frameNumberText, org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('webcam stereo image', frameStereo)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        imageName = 'webcam_stereo_image_%i.jpg' %count
        cv2.imwrite(imageName, frameStereo, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('%s isimli resim başarıyla kaydedildi.' %imageName)
        count = count+1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap0.release()
cap1.release()
cv2.destroyAllWindows()