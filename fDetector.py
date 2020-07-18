import  cv2

class faceDetector():
    """ yüz tespiti sınıfı  """
    def __init__(self, cascadePath):
        #  eğitilmiş modelin yüklenmesi
        self.fCascade = cv2.CascadeClassifier(cascadePath)

    def detectFace(self, img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        #  görüntüdeki yüzlerin tespiti
        #  scaleFactor: her defasında %10-1.1(%5-1.05) farklı şekillerde pencere(görünüt) boyutunu azaltma
        #  minNeighbors: sınıflandırıcının görüntü üzerinde tespit edilebilir minimum pencere sayısı
        #  minSize: minumu pencere büyüklüğü
        rects = self.fCascade.detectMultiScale(img, scaleFactor=scaleFactor,
                                               minNeighbors=minNeighbors,
                                               minSize=minSize,
                                               flags=cv2.CASCADE_SCALE_IMAGE)
        #  tespit edilen çevreleri geri döndürür
        return rects

