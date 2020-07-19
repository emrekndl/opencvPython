import cv2
from fDetector import faceDetector
#  import imutils

# fDetector ile cascade modelinin yüklenmesi
f = faceDetector("cascades/haarcascade_frontalface_default.xml")

#  videonun yüklenmesi -> video yolu -> videos/vlc-record.mp4
#  webcam -> 0
cam = cv2.VideoCapture(0)

#  videodaki frame leri(görüntüleri) alabilmek için döngü
while  True:
    #  kameredan yada videodan görüntülerin frame olarak alınması
    #  grabbed: frame in alınıp alınmadığı bilgisini tutar(True/False)
    (grabbed, frame) = cam.read()
    #  frame in boyutunun ayarlanması
    #  büyük boyutlu görüntülerde yavaşlama olmasını engellemek için
    #  frame = imutils.resize(frame, 500)
    #  görünütünün griye çevrilmesi, tek boyuta
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # görüntüden yüzlerin bulunması
    f = faceDetector("cascades/haarcascade_frontalface_default.xml")
    faceRects = f.detectFace(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #  frame in kopyası alınır çoğaltılır
    frame2 = frame.copy()

    print(f"Bulunan yüz sayısı: {len(faceRects)}")

    #  döngü ile bulunan yüzlerin etrafını çizdirme
    for (x, y, w, h) in faceRects:
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (255, 0, 0,), 2)

    #  tespit edilen yüzlerin gösterilmesi
    cv2.imshow("Yuzler", frame2)
    #  döngüden çıkımak için
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# kameranın kapatılması
cam.release()
cv2.destroyAllWindows()
