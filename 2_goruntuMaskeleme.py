import cv2
import numpy as np

#  görüntü yükleme
img = cv2.imread("images/cellphone.png")
cv2.imshow("Orijinal", img)

print(f"goruntu sekli: {img.shape}") #  (350, 370, 3), [:2] -> (350, 370)
# 0 lardan oluşan orijanl görüntü şeklinde maske oluşturuluyor.
maske = np.zeros(img.shape[:2], dtype=np.uint8)
#  görüntü merkezini bulma, x ve y noktalarını 2 ye bölme
(gmX, gmY) = (img.shape[1]//2, img.shape[0]//2)
print(f"gmX: {gmX}, gmY: {gmY}")

maske2 = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.circle(maske2, (gmX, gmY), 100, 255, -1)
maskelenmisG2 = cv2.bitwise_and(img, img, mask=maske2)

cv2.imshow("Maske", maske2)
cv2.imshow("Maskelenmis Goruntu", maskelenmisG2)

cv2.waitKey(0)

# dikdörtgen oluşturma (görüntü,başlsngıç noktası, bitiş noktası, renk, içi dolu)
cv2.rectangle(maske, (gmX-100, gmY-100), (gmX+100, gmY+100), 255, -1)
#cv2.imshow("Maske", maske)
maskelenmisG = cv2.bitwise_and(img, img, mask=maske)
cv2.imshow("Maske", maske)
cv2.imshow("Maskelenmis Goruntu", maskelenmisG)

cv2.waitKey(0)
