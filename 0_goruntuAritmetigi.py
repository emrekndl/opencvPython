import cv2
import numpy as np

#  görüntü yükleme
img = cv2.imread("images/digit_sample.png")
cv2.imshow("Orijinal", img)

#  opencv matris toplamada 0-250 limitdir.
#  Sonuç 250den fazla ise 250, 0 dan az ise 0 alınır.
print(f"opencv max: {cv2.add(np.uint8([200]), np.uint8([100]))}")
print(f"opencv min: {cv2.subtract(np.uint8([50]), np.uint8([100]))}")

#  numpy mattris toplamada 256 mod alınır.
print(f"numpy(mod) max: {np.uint8([200])+np.uint8([100])}")
print(f"numpy(mod) min: {np.uint8([50])-np.uint8([100])} \n")

cv2.waitKey(0)


print(f"Orijinal goruntu sekli: {img.shape} goruntu tipi: {img.dtype}")
#  Orijinal görüntü şeklinde ve tipinde
#  100 lerden oluşan bir matris oluşturuldu.
matris = np.ones(img.shape, img.dtype)*100
#  Oluşturulan matris orijinal görüntüye eklendi.
ekleme = cv2.add(img, matris)
cv2.imshow("Ekleme", ekleme)

#  Orijinal görüntü şeklinde ve tipinde
#  50 lerden oluşan bir matris oluşturuldu.
matris = np.ones(img.shape, img.dtype)*50
#  Oluşturulan matris orijinal görüntüden çıkarıldı.
cikarma = cv2.subtract(img, matris)
cv2.imshow("Cikarma",cikarma)

cv2.waitKey(0)

#  0 -> siyah, 255 -> beyaz olduğundan çıkarma işeleminde
#  değerler 0 a yaklaştığında görüntü karardı.
#  Ekleme işleminde değerler 255 e yaklaştığından görüntü beyazlaştı.
