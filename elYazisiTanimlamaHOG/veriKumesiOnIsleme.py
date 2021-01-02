import numpy as np
import mahotas
import cv2
from resize import imgResize

def load_data(datasetPath):
    #  veri kümesini 8 bitlik numpy array e çevirir
    data = np.genfromtxt(datasetPath, delimiter=",", dtype="uint8")
    #  hedef ilk sütın rakamlar seçilir
    target = data[:, 0]
    data = data[:, 1:].reshape(data.shape[0], 28, 28)

    return (data, target)

#  eğik görüntülerin düzeltilmesi(eğrilik düzeltme-deskew)
def deskew(img, width):
    #  görüntünün boyutları alınır
    (h, w) = img.shape[:2]
    #  momentler görüntüdeki beyaz piksellerin konumunun dağılımını verir
    moments = cv2.moments(img)
    #  merkezi momentler mu11,mu02 (skew - eğri)
    #  Görüntüyü çarpıtmak için mu11 varyansına göre x ekseninde (mu02) çarpıklık kullanılır
    skew = moments["mu11"] / moments["mu02"]
    #  momentlere ve çarpıtma matrislerine göre eğim hesaplanır
    M = np.float32([
        [1, skew, -0.5*w*skew],
        [0, 1, 0]])
    #  eğri giderme (eğriltilicek görüntü, görüntünün çarpıltılacağı yönü tanımlayan matris M,
    #  (eğimi giderilmiş görüntünün boyutu),eğri düzeltme metodu)
    image = cv2.warpAffine(img, M, (w, h), flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    #  eğrisi düzeltilmiş görüntü yeniden boyutlandırılır
    image = imgResize(image, width=width)

    return image

#  görüntünün kapsamını tanımlama
def center_extent(img, size):
    #  görüntünün çıktı boyutu
    (eW, eH) = size
    #  görüntünün genişliğinin yüksekliğinden büyüklüğü kontrol edilir
    #  ve yeniden boyutlandırılır
    if img.shape[1] > img.shape[0]:
        img = imgResize(img, width=eW)
    else:
        img = imgResize(img, height=eH)
    #  görüntünün boyutunda boşluk
    extent = np.zeros((eH, eW), dtype="uint8")

    #  görüntünün kapsamda yerleştirileceği yerin başlangıç koordinatları
    offsetX = (eW  - img.shape[1]) // 2
    offsetY = (eH - img.shape[0]) // 2
    #  gerçek kapsam
    extent[offsetY:offsetY + img.shape[0], offsetX:offsetX + img.shape[1]] = img
    # rakamı görüntünün ortasına yerleştirilecek şekilde çevirme
    #  görüntüdeki beyaz piksellerin ağırlıklı ortalamasını hesaplama
    #  -> görüntünün merkezinin ağırlıklı x, y koordinatları
    CM = mahotas.center_of_mass(extent)
    #  float değerleri tamsayılara dönüştürme
    (cY, cX) = np.round(CM).astype("int32")
    #  rakam görüntünün ortasına yerleştirilecek şekilde çevrilir
    (dX, dY) = ((size[0] // 2) - cX, (size[1]  // 2) - cY)
    M = np.float32([[1, 0, dX], [0, 1, dY]])
    extent = cv2.warpAffine(extent, M, size)

    #  ortalanmış görüntü geri döndürülür
    return extent

