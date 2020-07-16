import cv2
import matplotlib.pyplot as plt

#  görüntü yükleme
img = cv2.imread("images/maviTren.jpg")
cv2.imshow("Orijinal", img)
# %%
#  görüntüyü renk kanaallarına(b,g,r) ayırma
renkKanallari = cv2.split(img)
print(renkKanallari)
renkler = ["b", "g", "r"]

#  plt.figure()
#  grafik başlığı
plt.title("Renk Kanallarinin Histogrami")
#  x ekseninin başlığı
plt.xlabel("Kutular(Bins)")
#  y ekseninin başlığı
plt.ylabel("Piksel Sayıları")

#  mavi, yeşil, kırmızı renk kanllarının historamını çizdirnme
for kanal, renk in zip(renkKanallari, renkler):
    histogram = cv2.calcHist([kanal], [0], None, [256], [0, 256])
    plt.plot(histogram, color=renk)
    plt.xlim([0, 256])

#  plt.show()
#  cv2.waitKey(0)

#  histogramları tek figürde göstermek için subplot ekleme
#  1e 3 lük düzlemde ilk eleman 1-3
fig, axes = plt.subplots(nrows=1, ncols=3)
#  iki kanalı, yeşil ve mavi histogramı çizdirme
histogram1 = cv2.calcHist([kanal[1], kanal[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
axes[0].set_title("Yesil-Mavi")
#  nearest küçük görüntülerde, none büyük görüntülerde
plt.colorbar(axes[0].imshow(histogram1, interpolation="nearest"), ax=axes[0])

#  iki kanalı, yeşil ve kırmızı histogramı çizdirme
histogram2 = cv2.calcHist([kanal[1], kanal[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
axes[1].set_title("Yesil-Kirmizi")
plt.colorbar(axes[1].imshow(histogram2, interpolation="nearest"), ax=axes[1])

#  iki kanalı, mavi ve kırmızı histogramı çizdirme
histogram3 = cv2.calcHist([kanal[0], kanal[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
axes[2].set_title("Mavi-Kirmizi")
plt.colorbar(axes[2].imshow(histogram3, interpolation="nearest"), ax=axes[2])


print(f"iki kanalli histogram sekli: {histogram3.shape} ve değerleri: {histogram3.flatten().shape[0]}")

hist3K = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print(f"uc kanalli histogram sekli: {hist3K.shape} ve değerleri: {hist3K.flatten().shape[0]}")

plt.tight_layout()
plt.show()
cv2.waitKey(0)
