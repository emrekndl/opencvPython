import cv2

#  çiçek görüntülerinin 3 boyutlu rgb histogramı, çiçek yapraklarının rengini karakterize etmek için kullanılacak
class RGBHistogram():
    def __init__(self, bins):
        #  3 boyutlu histogram için bölme sayısını içeren liste
        self.bins = bins

    def describe(self, img, mask = None):
        #  maske kullanılarak görütünün arka planını ayrılır, sadece çiçeği alınır
        hist = cv2.calcHist([img], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])
        #  normalleştirme
        cv2.normalize(hist, hist)

        #  özellik vektörü döndürülür
        return hist.flatten()
