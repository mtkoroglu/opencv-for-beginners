import cv2
picture = cv2.imread('abc.jpg')
print(picture.shape[0])
print(picture.shape[1])
picture = cv2.resize(picture, (int(picture.shape[1]/2), int(picture.shape[0]/2)),
interpolation = cv2.INTER_AREA)
cv2.imshow('resim', picture)
cv2.waitKey(0)