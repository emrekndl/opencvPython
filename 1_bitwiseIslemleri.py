import cv2
import numpy as np

#  dikdortgen oluşturma,
#  0 lardan oluşan 200, 200 boyutunda görüntü(tuval,canvas) oluşturuldu.
#  (görüntü, başlangıç noktası, bitiş noktası, renk, içi dolu)
dikdortgen = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(dikdortgen, (20, 20), (180, 180), 255, -1)
cv2.imshow("Dikdortgen", dikdortgen)
cv2.waitKey(0)

#  daire oluşturma,
#  (görüntü, merkez noktası, yarı çapı, renk, içi dolu)
daire = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(daire, (100, 100), 100, 255, -1)
cv2.imshow("Daire", daire)
cv2.waitKey(0)

#  if piksel == 0 piksel = kapalı
#  if piksel > 0 piksel = açık

#  bitwise and
#  her iki piksel değeri de 0 dan büyükse, piksel açık
#  her iki piksel değeri de 0 a eşitse , piksel kapalı
#  dikdörtgenin ve dairenin ortak alanlarını buluyor.
bitwiseAnd = cv2.bitwise_and(dikdortgen, daire)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)
#  bitwise or
#  her ikisinin bulunduğu alanlar
bitwiseOr = cv2.bitwise_or(dikdortgen, daire)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
#  bitwise xor
#  her ikisi doğruysa piksel kapalı(1-1,0-0)
# ortak olmayan alanları
bitwiseXor = cv2.bitwise_xor(dikdortgen, daire)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)
#  bitwise not
#  piksel 0 -> 255 , piksel > 0 -> 0 tersini alma
bitwiseNot = cv2.bitwise_not(daire)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
