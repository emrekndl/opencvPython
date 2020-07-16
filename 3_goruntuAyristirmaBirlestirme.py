import cv2
import numpy as np

#  görüntü yükleme
img = cv2.imread("images/cellphone.png")
cv2.imshow("Orijinal", img)

#  Görüntüyü RGB renk katmanlarına ayırma
(B, G, R) = cv2.split(img)

cv2.imshow("RED", R)
cv2.imshow("GREEN", G)
cv2.imshow("BLUE", B)

cv2.waitKey(0)
#  Renk katmanlarını tek resimde birleştirme
birlestirme = cv2.merge([B, G, R])
cv2.imshow("Birlestirme", birlestirme)

cv2.waitKey(0)
#  Orijinal görüntü şeklinnde 0 lardan oluşan matris oluşturuluyor
zeros = np.zeros(img.shape[:2], dtype=np.uint8)
#  görüntünün RGB katmanlarını ayrı ayrı matrislerde gösterme
cv2.imshow("RED", cv2.merge([zeros, zeros, R]))
cv2.imshow("GREEN", cv2.merge([zeros, G, zeros]))
cv2.imshow("BLUE", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
