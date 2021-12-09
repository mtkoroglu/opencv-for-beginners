import cv2
resim = cv2.imread('giraffe.jpg', cv2.IMREAD_COLOR)
##################### resmi değişik filtrelerden geçir ############################
k = 25
fresim1 = cv2.blur(resim, [k, k])
fresim2 = cv2.GaussianBlur(resim, [k, k], 0)
fresim3 = cv2.medianBlur(resim, k)
fresim4 = cv2.bilateralFilter(resim, 49, 85, 95)
########## ekranda görüntüleyebilmek için resmi yeniden boyutlandır ###############
s = 1/6
dim = (int(s*resim.shape[1]), int(s*resim.shape[0]))
resim0 = cv2.resize(resim, dim, cv2.INTER_LINEAR)
resim1 = cv2.resize(fresim1, dim, cv2.INTER_LINEAR)
resim2 = cv2.resize(fresim2, dim, cv2.INTER_LINEAR)
resim3 = cv2.resize(fresim3, dim, cv2.INTER_LINEAR)
resim4 = cv2.resize(fresim4, dim, cv2.INTER_LINEAR)
####################### resimleri ekranda görüntüle ###############################
cv2.imshow('original', resim0)
cv2.imshow('cv2.blur()', resim1)
cv2.imshow('cv2.GaussianBlur()', resim2)
cv2.imshow('cv2.medianBlur()', resim3)
cv2.imshow('cv2.bilateralFilter()', resim4)
cv2.waitKey(0) # kullanıcı klavyeden herhangi bir tuşa basana kadar bekle
########################## resimleri dosyaya yaz ###################################
cv2.imwrite('giraffe blur.jpg', fresim1, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe GaussianBlur.jpg', fresim2, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe medianBlur.jpg', fresim3, [cv2.IMWRITE_JPEG_QUALITY, 100])
cv2.imwrite('giraffe bilateralFilter.jpg', fresim4, [cv2.IMWRITE_JPEG_QUALITY, 100])
