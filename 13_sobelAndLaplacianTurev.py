import numpy as np
import cv2

#  Gradient Sobel - Laplacian
# Türev kullanarak, piksel yoğunluğunun keskin olarak değiştiği noktaları bulma

img = cv2.imread("images/coins.png")
# görüntüyü tek kanala çevirme
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Goruntu", img)

#  Laplacian
#  grin görüntüye çevrilmesinin nedeni
#  siyahtan beyaza geçen yerlerde eğim pozitif
#  beyazdan siyaha geçen yerlerde eğim negatif
#  görüntü, 64 bitlik float(türev negatif olabilir)
lap = cv2.Laplacian(img, cv2.CV_64F)
print("64F: ",lap)
#  türevin mutlak değeri alınıp 8 bite çevrilir
lap = np.uint8(np.absolute(lap))
print("uint8-absolute: ", lap)
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

#  Sobel
#  dikey kenar tespiti
#  x ekseninde türev
#  görüntü, 64 bit float, x ekseni 1, 0
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #  vertical edge
#  yatay kenar tespiti
#  y ekseninde türev
#  görüntü, 64 bit float, y ekseni 0, 1
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) #  horizantal edge
#  mutlak değeri alma
sobelX =  np.uint8(np.absolute(sobelX))
sobelY =  np.uint8(np.absolute(sobelY))

#  x ekseni ve y eksenini birleştrme
sobelCombined = cv2.bitwise_xor(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

