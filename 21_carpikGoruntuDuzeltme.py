import cv2
import  numpy as np

img = cv2.imread("images/card.jpg")

#  yeni görüntünün boyutları
width, height = 410, 550

#  düzeltilecek görüntünün köse noktaları
pts = np.float32([[168, 317], [319, 210], [332, 561], [489, 457]])
#  yeni görüntünün boyutları
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

#  görüntününü kuş bakışı görünümünü elde etmek için
#  perspektif dönüşüm matrisi kullanılır
#  (orijinal görüntüdeki 4 roi(ilgili alan) noktaları, dönüştürülmüş noktalları)
matrix = cv2.getPerspectiveTransform(pts, pts2)
#  yeni görünütünün oluşturulması
#  (orijinal görüntü, dönüşüm matrisi, çıktı görüntüsünün genişliği ve yüksekliği)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

#  köşe noktaların görüntü üzerinde gösterilmesi
for i in range(0, 4):
    cv2.circle(img, (pts[i][0], pts[i][1]), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("orjinal goruntu", img)
cv2.imshow("duzeltilmis goruntu", imgOutput)

cv2.waitKey(0)
