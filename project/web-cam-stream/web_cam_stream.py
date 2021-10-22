import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read() # Capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (T, bw) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('bgr image.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        cv2.imwrite('gray scale image.jpg', gray, [cv2.IMWRITE_JPEG_QUALITY, 100])
        cv2.imwrite('thresholded image.jpg', bw, [cv2.IMWRITE_JPEG_QUALITY, 100])
        break
cap.release()
cv2.destroyAllWindows()
