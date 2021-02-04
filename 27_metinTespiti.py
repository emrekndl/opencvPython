import cv2
import  pytesseract

#  görüntünün yüklenmesi
img = cv2.imread("ocrimage.png")
#  görüntünün rgb ye çevrilmesi
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#  görüntüdeki metinleri bulma
#  print(pytesseract.image_to_string(img))

#  görüntüdeki karakterlerin alanlarının koordinatlarının verir
#  print(pytesseract.image_to_boxes(img))

#  Karakter Tespiti
hImg, wImg, _ = img.shape
#  karakter alanları
boxes = pytesseract.image_to_boxes(img)

for  i in boxes.splitlines():
    i = i.split()
    #  print(i)
    x, y, w, h = int(i[1]), int(i[2]), int(i[3]), int(i[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 255, 0), 2)
    cv2.putText(img, i[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (50, 50, 255), 2)


"""
#  Kelime Tespiti
hImg, wImg, _ = img.shape
#  kelimelerin ayrıntılı alanları
boxes = pytesseract.image_to_data(img)

for  i,j in enumerate(boxes.splitlines()):
    if i != 0:
        j = j.split()
        #  print(i)
        if len(j) == 12:
            x, y, w, h = int(j[6]), int(j[7]), int(j[8]), int(j[9])
            cv2.rectangle(img, (x, y), (w +x, h + y), (0, 255, 0), 2)
            cv2.putText(img, j[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (50, 50, 255), 2)
"""
"""
#  Rakam Tespiti
hImg, wImg, _ = img.shape
#  oem 3 => OEM_DEFAULT(0-> sadece tesseract çalıştırma, hızlı, 1-> sadece Cube çalıştıurma, daha iyi kalite, yavaş)(0-3)
#  psm 6 => PSM_SINGLE_BLOCK, metin etrafında tek blok oluşturma (0-13)
#  rakam tespiti için ayarlama
conf = r"--oem 3 --psm 6 outputbase digits"
#  kelimelerin ayrıntılı alanları
boxes = pytesseract.image_to_data(img, config=conf)

for  i,j in enumerate(boxes.splitlines()):
    if i != 0:
        j = j.split()
        #  print(i)
        if len(j) == 12:
            x, y, w, h = int(j[6]), int(j[7]), int(j[8]), int(j[9])
            cv2.rectangle(img, (x, y), (w +x, h + y), (0, 255, 0), 2)
            cv2.putText(img, j[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (50, 50, 255), 2)

"""


cv2.imshow("sonuc", img)

cv2.waitKey(0)


