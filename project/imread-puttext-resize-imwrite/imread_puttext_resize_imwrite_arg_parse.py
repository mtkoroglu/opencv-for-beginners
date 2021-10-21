import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print('Image size is:')
print(image.shape)
# write text on image
font = cv2.FONT_HERSHEY_SIMPLEX # font
# Bottom-left corner of the text string in the image
org = (1300, 300) # (550, 300) 
fontScale = 7
color = (255, 255, 255) # BGR order
thickness = 12 # Line thickness of 2 px
imageText = cv2.putText(image, 'Silvercity', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imwrite('Silvercity.jpg', imageText, [cv2.IMWRITE_JPEG_QUALITY, 97])
# resize images and display
nOfCols = 360.0
r = nOfCols / image.shape[1]
dim = (int(nOfCols), int(image.shape[0]*r))
resizedImageText = cv2.resize(imageText, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('Silvercity_resized.jpg', resizedImageText, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imshow("resized image with text", resizedImageText)
cv2.waitKey(0)
