import cv2
import numpy as np
from stackImages import stackImages

FRAMEWIDTH = 640
FRAMEHEIGHT = 480

camera = cv2.VideoCapture(0)
camera.set(3, FRAMEWIDTH)
camera.set(4, FRAMEHEIGHT)

def nothing():
    pass

#  şekil kenarlarını bulabilmek için threshold ve alan değerleri trackbar
cv2.namedWindow("Parametreler")
cv2.resizeWindow("Parametreler", 640, 240)
cv2.createTrackbar("Threshold1", "Parametreler", 98, 255, nothing)
cv2.createTrackbar("Threshold2", "Parametreler", 255, 255, nothing)
cv2.createTrackbar("Alan", "Parametreler", 5000, 30000, nothing)

#  giriş görüntüsünün şekil hatlarını bulamak için
def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Alan", "Parametreler")

        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (0, 220, 255), 7)
            #  köse noktalrını bulma( true-> kapalı contor)
            param = cv2.arcLength(cnt, True)
            #  şeklin tipini bulma (contor, çözünürlük, kapalı contor)
            approx = cv2.approxPolyDP(cnt, 0.02 * param, True)
            print(len(approx))

            #  bulunan şekilleri kare içine alma
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 179, 102), 5)

            #  nokta ve alan sayısının yazdırılması
            cv2.putText(imgContour, "Nokta: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 2)
            cv2.putText(imgContour, "Alan: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 2)

while True:
    grabbed, frame = camera.read()
    imgContour = frame.copy()

    #  görüntü bulanıklaştırma
    imgBlur = cv2.GaussianBlur(frame, (7, 7), 1)
    #  griye çevirme
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    #  trackbar dan gelen değerleri alma
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parametreler")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parametreler")
    #  canny ile kenar tespiti
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    #  gürültüleri temizlemek için dilate fonksiyonu
    #  dilate için kernel
    kernel = np.ones((5, 5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)

    #  şekil çevrelerini bulma
    getContours(imgDilate, imgContour)

    #  sonuçların gösterimesi
    cv2.imshow("sekil tespiti", stackImages(0.6, ([frame, imgBlur, imgGray],
                                                  [imgCanny, imgDilate, imgContour])))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
