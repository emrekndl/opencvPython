import cv2
import numpy as np

circles = np.zeros((4,2), np.int)
counter = 0

def mousePoints(event, x, y, flags, param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)


img = cv2.imread("images/book.jpg")
imgCopy = img.copy()
while True:
    if counter == 4:
        width, height = 410, 550

        #  düzeltilecek görüntünün köse noktaları
        pts = np.float32([circles[0], circles[1], circles[2], circles[3]])
        #  yeni görüntünün boyutları
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        #  perspektif matrisi
        matrix = cv2.getPerspectiveTransform(pts, pts2)
        #  yeni görünütünün oluşturulması
        imgOutput = cv2.warpPerspective(imgCopy, matrix, (width, height))
        cv2.imshow("duzeltilmis goruntu", imgOutput)


    #  köşe noktaların görüntü üzerinde gösterilmesi
    for i in range(0, 4):
        cv2.circle(img, (circles[i][0], circles[i][1]), 4, (0, 0, 255), cv2.FILLED)


    cv2.imshow("orijinal goruntu", img)
    cv2.setMouseCallback("orijinal goruntu", mousePoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




"""
circles = np.zeros((4, 2), np.int)


def mousePoints(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(str(param))
        circles[0] = x, y
        print("calisti1")


width, height = 250, 350
img = cv2.imread("images/book.jpg")


param = 0
while  True:
    cv2.imshow("orijinal goruntu", img)
    print(param)
    cv2.setMouseCallback("orijinal goruntu", mousePoints, param)
    if param <= 3:
        cv2.circle(img, (circles[param][0], circles[param][1]), 5, (0, 255, 0), cv2.FILLED)
        param += 1
    if param == 3:
        print(circles)
        cv2.imshow("orijinal goruntu", img)
        pts = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))

        cv2.imshow("duzeltilmis goruntu", imgOutput)

cv2.waitKey(1)"""
