import cv2
import numpy as np
from stackImages import stackImages

FRAMEWIDTH = 640
FRAMEHEIGHT = 480
#  kamera çerçevesinin boyutları
camera = cv2.VideoCapture(0)
camera.set(3, FRAMEWIDTH)
camera.set(4, FRAMEHEIGHT)

#  Trackbar tanımlaması için gerekli boş fonksiyon
def nothing(x): pass

#  HSV değerlerini değiştirebilmek için oluşturlan track bar lar
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)

#  track bar adı, hangi pencerede görüneceği, aralık değerleri, fonksiyon
cv2.createTrackbar("HUE Min", "HSV", 0, 179, nothing)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, nothing)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, nothing)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, nothing)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, nothing)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, nothing)


while True:
    #  kameradan görüntünün alınması
    _, frame = camera.read()
    #  görüntünün hsv ye dönüştürülmesi
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #  oluşturulan track bar değerlerinin değişkenlere aktarılması
    hMin = cv2.getTrackbarPos("HUE Min", "HSV")
    hMax = cv2.getTrackbarPos("HUE Max", "HSV")
    SATMin = cv2.getTrackbarPos("SAT Min", "HSV")
    SATMax = cv2.getTrackbarPos("SAT Max", "HSV")
    VALUEMin = cv2.getTrackbarPos("VALUE Min", "HSV")
    VALUEMax = cv2.getTrackbarPos("VALUE Max", "HSV")

    #  hsv değerlerinin alt ve üst limitlerinin berlirlenmesi
    lower = np.array([hMin, SATMin, VALUEMin])
    upper = np.array([hMax, SATMax, VALUEMax])

    #  belirnen limit değerleri ile maske oluşturlması
    mask = cv2.inRange(imgHSV, lower, upper)
    #  oluşturlan maskenin uygulanması
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #  stackImages ile görüntülerin birlikte gösterilmesi
    stackImgs = stackImages(0.5, ([frame, mask, result]))
    cv2.imshow("Renk Tespiti", stackImgs)

    #  cv2.imshow("HSV goruntu", imgHSV)
    #  cv2.imshow("orijinal goruntu", frame)
    #  cv2.imshow("Maske", mask)
    #  cv2.imshow("Sonuc", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
