import cv2
import numpy as np
from stackImages import stackImages


kernel = np.ones((5, 5), np.uint8)
print(kernel)

#  img = cv2.imread("images/lena.png", 0) -> gri görüntü
#img = cv2.imread("images/lena.png")
#img2 = cv2.imread("images/airplane.png")
#print(img.shape)
#print(img2.shape)

#img1 = cv2.resize(img, (0 ,0), None, 0.5, 0.5)
#img2 = cv2.resize(img2, (0 ,0), None, 0.5, 0.5)

#print(img1.shape)
#print(img2.shape)

#hor = np.hstack((img1, img2))
#ver = np.vstack((img1, img2))

#cv2.imshow("Horizontal-Yatay", hor)
#cv2.imshow("Vertical-Dikey", ver)

#  numpy horizontal stack -> . + . = ..
#  görüntü kanal sayısı aynı olamalı
#  numpy vertical stack -> . + . = :

#  eşit görüntü olmadığında kullanılır
#  imgBlank = np.zeros((200, 200), np.uint8)

#  webcam kullanımı
frameWıdth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWıdth)
cap.set(4, frameHeight)

while True:
    succes, img = cap.read()
    #  cv2.imshow("WebCam", img)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

    imgCanny = cv2.Canny(imgBlur, 100, 200)

    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)

    imgEroded = cv2.erode(imgDilation, kernel, iterations=2)


    #  normal kullanım
    #  cv2.imshow("Coklu Goruntu", stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgDilation, imgEroded])))
    cv2.imshow("Coklu Goruntu", stackImages(0.3, ([img, imgGray, imgBlur, img, imgGray, imgBlur],
                                                  [imgCanny, imgDilation, imgEroded, img, imgGray, imgBlur],
                                                  [imgCanny, imgDilation, imgEroded, img, imgGray, imgBlur],
                                                  [imgCanny, imgDilation, imgEroded, img, imgGray, imgBlur],
                                                  )))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



