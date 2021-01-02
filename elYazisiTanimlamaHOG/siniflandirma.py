import  joblib
from hogScikit import  HOG
from veriKumesiOnIsleme import deskew, center_extent
import mahotas
import  cv2

#  eğitilmiş modelin yüklenmesi
model = joblib.load("svm.cpickle")

#  hog eğitimde ki aynı parametreler ile oluşturulur
hog = HOG(orientations = 18, pixelsPerCell = (10, 10), cellsPerBlock = (1, 1), transform = True)
#  test edilecek görüntü yüklenir
img = cv2.imread("images/digit_sample.png")
#  görüntü griye çevrilir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  görüntü bulanıklaştırılır
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#  canny ile görüntüdeki kenarlar bulunur
edged = cv2.Canny(blurred, 30, 150)

#  kenarlı görüntüdeki şekil çevreleri(contours) bulunur ve soldan sağa doğru sıralınır,
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#  bu şekil çevrelerinin her biri, sınıflandırlması gereken bir görüntüdeki bir rakamı tesmsil eder
cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])

for (c, _) in cnts:
    #  her bir şekil çevresi için bir sınırlayıcı kutu hesaplanır
    (x, y, w, h) = cv2.boundingRect(c)
    #  en az 7 piksel genişliğinde ve 20 piksel yüksekliğinde sınırlayıcı kutununu boyutu kontrol edilir
    if w >= 7 and h >= 20:
        #  ilgi bölgesi(roi) gri tonlamalı görüntüden çıkartılır.
        #  roi sınıflandırılacak rakamı tutuyor
        roi = gray[y:y + h, x:x+ w]
        #  ön planı(rakamı) arka plandan(rakamın üzerine yazıldığı kağıt) ayırmak için otsu kullanılır
        thresh = roi.copy()
        T = mahotas.thresholding.otsu(roi)
        thresh[thresh > T] = 255
        thresh = cv2.bitwise_not(thresh)

        #  eğitimde ki gibi rakam daha sonra eğriltilir
        thresh = deskew(thresh, 20)
        #  görünütünün merkezine çevrilir
        thresh = center_extent(thresh, (20, 20))

        cv2.imshow("thresh", thresh)

        #  roi inin hog değeri hesaplanır
        hist = hog.describe(thresh)
        #  hog değerine bağlı olarak roi nin hangi rakam olduğunu tahmin eder
        digit = model.predict([hist])[0]
        #  tahmin edilen değer ekrana yazdırlır
        print(f"rakam tahmini : {digit}")

        #  orijinal görünütüde geçerli rakamların etrafına yeşil kutu çizilir ve tahmin değeri yazılır
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.putText(img, str(digit), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
        cv2.imshow("image", img)
        cv2.waitKey(0)
