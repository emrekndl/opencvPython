import cv2

#  Threshold-Eşikleme
#  thresholding: görünütünün binary(ikili) hale dönüştürülmesi

img = cv2.imread("images/coins.png")
cv2.imshow("Orijinal", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  bulanıklaştırma: keskinlikleri gidermek için
blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Blurred(Bulanik)", blurred)

#  bulanıklaştırılmış görüntü, eşik değeri 155, 255, eşikleme tipi
#  (155 den küçük piksel değerleri 0 ve diğer piksel değerleri 255  )
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
print("T: ", T, "\nthresh:", thresh)
cv2.imshow("Threshold Binary(İkili Esikleme)", thresh)

#  ters eşikleme
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse(Ters İkili Esikleme)", threshInv)

#  ters eşikleme kullanılarak maskeleme
cv2.imshow("Coins", cv2.bitwise_and(img, img, mask=threshInv))

cv2.waitKey(0)
