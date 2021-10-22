import cv2
image = cv2.imread('IMG_20210616_202539.jpg')
print('height = %i   width = %i   channels = %i' %(image.shape[0],image.shape[1],image.shape[2]))
# write text on image
font = cv2.FONT_HERSHEY_SIMPLEX # font
# Bottom-left corner of the text string in the image
org = (300, 300) # (550, 300) 
fontScale = 7 # font büyüklüğü
color = (0, 0, 0) # BGR order - yazının rengi
thickness = 12 # Yazının kalınlığı
imageText = cv2.putText(image, 'Gumushane', org, font, fontScale, color, thickness, cv2.LINE_AA)
# resize images and display
s = 0.2 # scale - ölçek
dim = (int(s*image.shape[1]), int(s*image.shape[0]))
resizedImageText = cv2.resize(imageText, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('Gumushane.jpg', resizedImageText, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("Resized image with text", resizedImageText)
cv2.waitKey(0)