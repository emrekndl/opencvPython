from  skimage import  feature

#  Yönlendirilmiş Degradelerin Histogramı (HOG)
#  Kenar yönlendirme histogramlarına ve SIFT gibi yerel değişmez tanımlayıcılara benzer şekilde,
#  HOG görüntünün gradyan büyüklüğünde çalışır.
#  Bununla birlikte, görüntünün küçük, lokalize alanlarındaki kenarların oryantasyonu
#  üzerinden bir histogramı hesaplayan SIFT'ten farklı olarak, HOG
#  bu histogramları tekdüze aralıklı hücrelerden oluşan yoğun bir
#  ızgara üzerinde hesaplar. Ayrıca bu hücreler,
#  tanımlayıcının doğruluğunu artırmak için üst üste binebilir ve kontrast normalleştirilebilir.
class HOG:
    """
    parametreler:
    * orientations -> yönelim,her histogramdaki yönelim derecesi(bölme sayısı)
    * pixelsPerlCell -> her bir hücreye düşecek piksel sayısının tanımlar
    HOG tanımlayıcısını bir görüntünün üzerinde koyarken, görüntü her biri
    "pixelsPerlCell x pixselPerlCell" boyutundunda birden çok hücreye bölüncektir.
    Daha sonra her bi hücre için gradyan büyüklüklerinin bir histogramı hesaplanacaktır.
    * Sonra her bir bloğa düşen  hücre sayısına göre, her bir histogramı, cellsPerBlock argümanını kullanarak normalleştirir.
    (giriş görüntüsünün log u / karakökü) bu da tanımlayıcının daha iyi doğru sonuç vermesini sağlar.
    """
    def __init__(self, orientations=9, pixelsPerCell = (8, 8), cellsPerBlock = (3, 3), transform = False):
        self.orientations = orientations
        self.pixelsPerCell = pixelsPerCell
        self.cellsPerBlock = cellsPerBlock
        self.transform = transform

    def describe(self, img):
        hist = feature.hog(img, orientations = self.orientations,
                           pixels_per_cell = self.pixelsPerCell,
                           cells_per_block = self.cellsPerBlock,
                           transform_sqrt = self.transform)
        return hist

