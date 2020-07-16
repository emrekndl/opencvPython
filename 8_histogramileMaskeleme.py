import cv2
import matplotlib.pyplot as plt
import numpy as np

#  histogram çizdirme fonksiyonu
def histogramPlot(img, title, maske=None):
    kanallar = cv2.split(img)
    renkler = ["b", "g", "r"]
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].set_title(title)
    axes[0].set_xlabel("Kutular")
    axes[0].set_ylabel("Piksel Sayilari")

    for (kanal, renk) in zip(kanallar, renkler):
        histogram = cv2.calcHist([kanal], [0], maske, [256], [0, 256])
        axes[0].plot(histogram, color=renk)
        axes[0].set_xlim([0, 256])

    axes[1].set_title("Goruntu")
    #  plot imshow, rgb ile çalıştığından görüntü bgr dan rgb ye çevrildi.
    axes[1].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[1].axis("off")
    #cv2.imshow("o", img)
    plt.tight_layout()
    #plt.show()

def main():
    img = cv2.imread("images/maviTren.jpg")
    #cv2.imshow("orijinal", img)
    histogramPlot(img, "Orijinal Goruntunun Histogrami")
    #cv2.waitKey(0)

    maske = np.zeros(img.shape[:2], dtype="uint8")
    cv2.circle(maske, (513, 156), 80, 255, -1)
    cv2.imshow("Maske", maske)

    maskeleme = cv2.bitwise_and(img, img, mask=maske)
    cv2.imshow("Maskeleme", maskeleme)
    histogramPlot(img, "Maskeli Goruntunun Histogrami", maske)

    plt.show()
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
