import cv2

def imgResize(img, width = None, height = None, inter = cv2.INTER_AREA):
    #  boyut
    dim = None
    #  görüntünün genişlik ve yüksekliğini alma
    (h, w) = img.shape[:2]

    #  yükseklik ve genişlik girilmemişse orjinal görüntüyü döndür
    if width is None and height is None:
        return img

    #  genişlik girilmemişse
    if width is None:
        #  yükseklik oranın hesaplanır
        r = height / float(h)
        #  boyut oluşturulur
        dim = (int(w*r), height)

    #  yükseklik girilmemişse
    else:
        #  genişliğin oranı hesaplanır
        r = width / float(w)
        #  boyut oluşturulur
        dim = (width, int(h*r))

    #  görüntü yeniden boyutlandırılır
    resized = cv2.resize(img, dim, interpolation = inter)

    return resized
