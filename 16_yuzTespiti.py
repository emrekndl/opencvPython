import cv2
from fDetector import faceDetector

#  görüntünün yüklenmesi
img = cv2.imread("images/lena.png")
#img = cv2.imread("images/obama.png")
#  bu görüntüde iki yüz tespiti oluyor,
#  bunun için scaleFactor değerini değiştirmeliyiz.
#  scaleFactor=1.2
#img = cv2.imread("images/messi.png")
#  görünütünün griye çevrilmesi, tek boyutta
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# görüntüden yüzlerin bulunması
f = faceDetector("cascades/haarcascade_frontalface_default.xml")
faceRects = f.detectFace(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Bulunan yüz sayısı: {len(faceRects)}")

#  döngü ile bulunan yüzlerin etrafını çizdirme
for (x, y, w, h) in faceRects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0,), 2)

#  tespit edilen yüzlerin gösterilmesi
cv2.imshow("Yuzler", img)
cv2.waitKey(0)
