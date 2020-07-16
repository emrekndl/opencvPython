import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/maviTren.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orijinal", img)
cv2.waitKey(0)
#  Gri görüntünün kontrast değerini düzenler.
histEqualize = cv2.equalizeHist(imgGray)
#  np.hstack iki görüntüyü gösterme
cv2.imshow("Histogram Esitleme", np.hstack([imgGray, histEqualize]) )
# matplotlib ile iki görüntüyü gösterme
plt.figure(figsize = (10, 5))
plt.subplot(1, 2, 1)
plt.title("Gri Goruntu")
plt.imshow(cv2.cvtColor(imgGray, cv2.COLOR_GRAY2RGB), aspect="auto")
#  görüntünün etrafındaki numaraları kaldırma
plt.axis("off")
plt.subplot(1, 2, 2)
plt.title("Histogram Esitlenmis Goruntu")
plt.imshow(cv2.cvtColor(histEqualize, cv2.COLOR_GRAY2RGB), aspect="auto")
plt.axis("off")
plt.tight_layout()
plt.show()

cv2.waitKey(0)
