import joblib
from  sklearn.svm import  LinearSVC
from hogScikit import  HOG
from  veriKumesiOnIsleme import load_data, center_extent, deskew

#  görünütülerden ve hedeflerden oluşan veri kümesini yükleme
(digits, target) = load_data("data/digits.csv")
#  her görünütünün hog değerlerini tutan liste
data = []

# gradyan büyüklüğü histogramı
hog = HOG(orientations = 18, pixelsPerCell = (10, 10), cellsPerBlock = (1, 1), transform = True)
#  rakam görüntülerinin üzerinde geçme
for  image in digits:
    #  eğriltiler
    image = deskew(image, 20)
    #  görüntünün ortasına çevrilir
    image = center_extent(image, (20, 20))

    #  hog değeri ön işlenmiş görünütü için hesaplanır
    hist = hog.describe(image)
    #  hog özellik vektörü listeye atılır
    data.append(hist)

#  rastgele durum kullanılarak somutlaştırılır
model = LinearSVC(random_state = 42)
#  model eğitilir
model.fit(data, target)

#  eğitilmiş model kaydedilir
joblib.dump(model, "svm.cpickle")

