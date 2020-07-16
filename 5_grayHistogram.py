import cv2
from matplotlib import pyplot as plt

#  görüntü yükleme
img = cv2.imread("images/cellphone.png")
#  görünütüyü tek kanala gri ye çevirme
#  gri görüntünün histogramını almak için griye çevrildi
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Gorontu", img)
cv2.waitKey(0)

#  histogram değerlerini hesaplama
#  (görüntü, tek kanal hesaplanacak ise 0, maske, x değerleri kaça bölünecek, piksel değerleri)
histogram = cv2.calcHist(img, [0], None, [256], [0, 256])

plt.figure()
#  grafik başlığı
plt.title("Grayscale Histogram")
#  x ekseninin başlığı
plt.xlabel("Kutular(Bins)")
#  y ekseninin başlığı
plt.ylabel("Piksel Sayıları")
#  görüntüyü figürde gösterme
plt.plot(histogram)
#  x ekseninin sınırı
plt.xlim([0, 256])
#  figürü gösterme
plt.show()

cv2.waitKey(0)

