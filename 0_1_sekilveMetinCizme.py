import cv2
import numpy as np

#  boş matris, sıfırlardan oluşan matris
#(boyut1, boyut2, kanal sayısı), int e çevirme
img = np.zeros((512, 512, 3), np.uint8)
#  0-255
print(img)
# BGR
#img[:] = 255, 0 ,0
#  Çizgi çizme
#  (görüntü,başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
#  dikdörtgen çizme
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)
#  daire ve çember çizme
#  (görüntü, merkez noktası, yarı çapı, renk, kalınlık(cv2.FILLED)
cv2.circle(img, (150 ,400), 50, (255, 0, 0), 3)

#  metin yazdırma
#  (görüntü, metin, konum, yazı tipi, yazı boyutu, renk, kalınlık)
cv2.putText(img, "Sekil Cizdirme", (75, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 150, 0), 1)

print(img.shape)

cv2.imshow("goruntu", img)
cv2.waitKey(0)
