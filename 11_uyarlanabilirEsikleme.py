import cv2

#  Threshold-Eşikleme
#  adaptive thresholding: görünütünün binary(ikili) hale dönüştürülmesi,
#  eşik değerinin uyarlanamsı, T değerinin otomatik olrak bulunması

img1 = cv2.imread("images/coins.png")
cv2.imshow("Orijinal", img1)
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Blurred(Bulanik)", blurred)
#  Thresh Mean: ortalama alarak bulma
#  11: kernel(pencere boyutu 11x11)boyutu komşuluk
#  4: find tuning-ince ayarlama, komşuluk ortalamasında
#  çıkarıldığında iyi sonuç alınınan değer
meanThresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", meanThresh)

#  Gaussian Thresh Yöntenmi
gausThresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", gausThresh)

#  eşikleme kullanılarak maskeleme
#  cv2.imshow("Coins", cv2.bitwise_and(img1, img1, mask=meanThresh))

cv2.waitKey(0)
