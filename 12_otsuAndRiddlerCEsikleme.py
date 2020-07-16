import  mahotas
import cv2

#  Threshold-Eşikleme
#  otsu thresholding: görüntüde iki zirve alıp,
#  optimum nokta-T yi bulmak için bu iki zirveyi birbirinden ayırır

img1 = cv2.imread("images/coins.png")
cv2.imshow("Orijinal", img1)
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Blurred(Bulanik)", blurred)

#  Otsu
#  Otsu T değeri bulma
T = mahotas.thresholding.otsu(blurred)
print(f"Otsu Threshold :{T}")
otsuThresh = img.copy()
#  piksel T den büyükse 255 beyaz atanır
otsuThresh[otsuThresh > T] = 255
#  255 den küçükse o siyah atanır
otsuThresh[otsuThresh < 255] = 0
#  threshold ınverse
otsuThresh = cv2.bitwise_not(otsuThresh)
cv2.imshow("Otsu Thresholding", otsuThresh)

#  Riddler Calvard
#  RC T değeri bulma
T = mahotas.thresholding.rc(blurred)
print(f"Riddleer Calvard Threshold :{T}")
rcThresh = img.copy()
rcThresh[rcThresh > T] = 255
rcThresh[rcThresh < 255] = 0
#  threshold ınverse
rcThresh = cv2.bitwise_not(rcThresh)
cv2.imshow("Riddler Calvard Thresholding", rcThresh)

#  eşikleme ile maskeleme
#cv2.imshow("Otsu Maskeleme",cv2.bitwise_and(img, img, mask=otsuThresh))
cv2.waitKey(0)
