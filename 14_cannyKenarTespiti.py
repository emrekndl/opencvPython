import  cv2

img =  cv2.imread("images/coins2.png")
#img =  cv2.imread("images/airplane.png")
#img =  cv2.imread("images/apple_phonenumber.png")
#   gri ye çevirme
img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  parazitleri kaldırmak için bulanıklık uygulanır
img =  cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Bulanik", img)

#  görüntü, eşik değerleri
# türev değeri 150 eden büyükse kenar var
# türev değeri 30 dan küçükse kenar yok
canny = cv2.Canny(img, 30, 150)  #30, 255)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
