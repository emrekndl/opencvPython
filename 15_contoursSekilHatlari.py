import cv2
import numpy  as  np

## Counters - Dış Hatları, Şeklin Çevresi

img =  cv2.imread("images/coins2.png")
#  img =  cv2.imread("images/apple_phonenumber.png")
#  gri ye çevirme
gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  parazitleri kaldırmak için bulanıklık uygulanır
blurred =  cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Gri ve Bulanik", blurred)

#  canny ile kenarların bulunması
edges = cv2.Canny(blurred, 30 ,150)
cv2.imshow("Kenarlar", edges)

#  findContours görüntüyü bozduğu için görüntünün kopyası alınır
#  görüntü, görüntünün dış çevresi alma, görüntünün köşegen dikey  yatay segmentlerini şıkıştırıp bileştirir
(counts, h) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#  print("hierarcy : ",h)
#  bulunan çevrelerin sayısı
print(f"Bulunan paraların sayisi: {len(counts)}")

#  Şekillerini çizdirme

coins = img.copy()
#  çevresini çizdirme
#  görüntü, çevre sayısı, -1 hepsini çizdirme(sadece biri için 2,3,4,5), çizdirme rengi, kalınlık
cv2.drawContours(coins, counts, -1, (0, 255, 0), 2)
cv2.imshow("Paralar", coins)
cv2.waitKey(0)

#  Çizdirilen Şekilleri Kesip Çıkarma

#  herbir çevre üzerinde geziliyor
for i, c in enumerate(counts):
    #  her çevre için dikdörtgen çizdirme
    #  x , y konumu, genişlik ve yükseklik konumu
    x, y, w, h = cv2.boundingRect(c)
    #  paraları yazdırma
    print(f"Para #{i+1}")
    #  çizdirilen dikdörtgen alanlarını görüntüden kesme
    coin = img[y:y+h, x:x+w]
    cv2.imshow("Para", coin)
    #  paraları çember şeklinde çıkarma
    # maske
    mask =  np.zeros(img.shape[:2], dtype=np.uint8)
    #  herbir çevre için çember çıkarma
    (centerX, centerY), radius = cv2.minEnclosingCircle(c)
    #  çemberi çizdirme
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    #  çemberi maskeden kesme
    mask = mask[y:y+h, x:x+w]
    #  paraları maskeleme
    cv2.imshow("Maskelenmiş Para", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)
