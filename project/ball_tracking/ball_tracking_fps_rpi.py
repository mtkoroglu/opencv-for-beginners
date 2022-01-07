# this code is taken from https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# modified for web cam ball tracking. The author of the code is Adrian Rosebrock.

import argparse
import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
from collections import deque
import time # ekranda fps değerini görüntülemek için

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
ap.add_argument("-f", "--fps", type=int, default=30,
	help="(most recent) number of frames for computing the average fps")
ap.add_argument("-c", "--camera", type=int, default=0, 
    help="camera selection: 0 for RPi cam, 1 for USB web cam")
args = vars(ap.parse_args())

frameNumber = 0 # görüntünün üzerinde hangi karede olduğumuzu görüntüleyelim
count = 0 # dosyaya resim kaydetmek istediğimizde ismi dinamik olarak değişsin
# define the lower and upper boundaries of the "green" ball in the 
# HSV color space, then initialize the list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"]) # ekranda son pts karedeki topun konumunu çizdirme
fps = deque(maxlen=args["fps"]) # dequ isimli veri yapısı ortalama fps'yi hesaplarken bize yardım edecek
prevFrameTime = 0 # önceki karenin yakalanma zamanı
newFrameTime = 0 # şimdiki karenin yakalanma zamanı

# initialize the video stream and allow the camera sensor to warm up
vs = VideoStream(src=args["camera"]).start()
# vs = VideoStream(usePiCamera=True, resolution=(640,480)).start()
time.sleep(2.0)
while(True):
    # grab the current frame
    frame = vs.read()
    # handle the frame from VideoCapture or VideoStream
    frame = frame[1] if args.get("video", False) else frame

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if frame is None:
        print('Kameraya erişimde sorun!')
        break
    else:
        frameNumber += 1
        raw, col = frame.shape[0], frame.shape[1]
    # goruntu islemeye baslayalim
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) # hsv uzayına geçtik çünkü rgb uzayında renk tespiti/takibi pratik değil
	# construct a mask for the color "green", then perform a series of 
    # dilations and erosions to remove any small blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    # find contours in the mask and initialize the current (x, y) 
    # center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
	# only proceed if at least one contour was found
    if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		# only proceed if the radius meets a minimum size
        if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
	# update the points queue
    pts.appendleft(center)
    # loop over the set of tracked points
    for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore them
        if pts[i - 1] is None or pts[i] is None:
            continue
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    # resmin üzerinde topu bulup çizdirdikten sonra fps'yi hesaplayalım
    newFrameTime = time.time() # şu andaki karenin zamanı
    fpsCurrent = 1/(newFrameTime-prevFrameTime)
    prevFrameTime = newFrameTime
    # fps değerlerinin tuttuğumuz dequ yapısındaki diziye yeni hesaplanan değeri ekle
    fps.appendleft(fpsCurrent)
    # anlık fps değeri çok zıpladığından ortalama fps değerini hesapla
    fpsAvg = np.mean(fps)

    # create fps number text
    fpsText = 'FPS = %i' %int(fpsCurrent)
    fpsAvgText = 'Avg FPS = %i' %int(fpsAvg)
    # displaying FPS number on the frame
    cv2.putText(frame, fpsText, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 
    (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, fpsAvgText, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, 
    (255, 255, 255), 2, cv2.LINE_AA)
    # display ball coordinates (in pixels) on the frame
    ballCoordinateText = 'x=%i y=%i' %(center[0], center[1])
    cv2.putText(frame, ballCoordinateText, (20, raw-20), 
    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # display frame number on the frame
    frameNumberText = 'Frame #%i' %frameNumber
    frame = cv2.putText(frame, frameNumberText, (col-250, 30), 
    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('green ball detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        imageName = 'top_takibi_%i.jpg' %count
        cv2.imwrite(imageName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print('%s isimli resim başarıyla kaydedildi.' %imageName)
        count += 1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        print('Program sonlandırıldı.')
        break
vs.release()
cv2.destroyAllWindows()