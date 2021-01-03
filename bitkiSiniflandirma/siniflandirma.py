from rgbHistogram import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report
import numpy as np
import glob
import  cv2

#  dışarıdan görüntü konumlarını yükleme
imagePaths = sorted(glob.glob("dataset/images" + "/*.png"))
maskPaths = sorted(glob.glob("dataset/masks" + "/*.png"))

#  veri matrisi
data = []
#  sınıf etiketleri
target = []

#  kanal başına 8 bölmeli renk histogramı
#  8 x 8 x 8 = 512 boyutlu bir özellik vektörü döndürür.
desc = RGBHistogram([8, 8, 8])

for (imagePath, maskPath) in  zip(imagePaths, maskPaths):
    #  görüntüleri yükleme
    img = cv2.imread(imagePath)
    #  maskeleri yükleme
    mask = cv2.imread(maskPath)
    #  maskeleri griye çevirme
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    #  renk histogramı maske ile uygulanır, özelikler alınır
    features = desc.describe(img, mask=mask)

    #  özellik vektörü kaydedilir
    data.append(features)
    #  çiçeğin türü(adı) etiket listesine eklenir
    target.append(imagePath.split("_")[-2])

#
targetNames = np.unique(target)
#  ilişkili sınıf etiketlerini kodlamak için kullanılır
#  model için türlerin(dizeler) tam sayılara dönüşütürülmesi için kullanılır.
le = LabelEncoder()
#  tür adlarını tam sayılara, her tür için bir kategoriye uyarlar ardından
#  dizelere karşılık gelen tam sayı sınıflarına dönüştürür.
target = le.fit_transform(target)

#  veri kümesini eğitim ve test olarak ayırma
#  tüm veri kümesinin %30 sunu test kümesi olarak belirler
#  rs 42, sonuçların daha sonraki çalışmalarda yeniden üretilebilmesi için kullanılır.
(trainData, testData, trainTarget, testTarget) = train_test_split(data, target, test_size = 0.3, random_state = 42)

#  birden çok karar ağacında oluşan, sınıflandırma için kullanılan toplu öğrenme yöntemi
#  25 karar ağacı kullanılır
model = RandomForestClassifier(n_estimators = 25, random_state = 84)

#  eğitim verileri kullanılarak eğitilir ve ardından test verileriyle karşılaştırılarak değerlendirilir.
model.fit(trainData, trainTarget)

#  modelin doğruluğunu yazdırma
print(classification_report(testTarget, model.predict(testData), target_names = targetNames))


#  test edilme için rastgele 10 görüntü alınır
for  i in np.random.choice(np.arange(0, len(imagePaths)), 10):
    imagePath = imagePaths[i]
    maskPath = maskPaths[i]

    img = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(img, mask)

    flower = le.inverse_transform(model.predict([features]))[0]
    print(imagePath)
    print(f"Bitki : {flower.upper()}")
    #  çiçeğin ekranda gösterilmesi
    cv2.imshow("image", img)
    cv2.waitKey(0)
