import argparse
import cv2
from fDetector import faceDetector

#  cascade dosyalarının eklenmesi
#  eğitilmiş modeller(yüz ve göz için)
def addCascade():
    #  faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
    eyeCascade = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")
    return eyeCascade

#  eklenen cascade dosyalarının üzerinden önce yüz ve sonra yüzün içinde gözlerin bulunması
def track(img, e):
    #  faceR = f.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    #  yüzlerin bulunması(tespit edilen çevreleri döndürür)
    face = faceDetector("cascades/haarcascade_frontalface_default.xml")
    faceR = face.detectFace(img)
    rects = []
    for (fx, fy, fw, fh) in faceR:
        #  faceROI yüzün sınırlayıcı alanını belirler(Region of Interest -İlgi Bölgesi(ROI))
        #  [fy den fy+fh ve fx den fx+fw kadar olan alan]
        faceROI = img[fy:fy+fh, fx:fx+fw]
        #  alanın noktalarını listeye ekleme
        rects.append((fx, fy, fx+fw, fy+fh))
        #  gözlerin bulunması
        #  scaleFactor: her defasında %10-1.1(%5-1.05) farklı şekillerde pencere(görüntü) boyutunu azaltma
        #  minNeighbors: sınıflandırıcının görüntü üzerinde tespit edilebilir minimum pencere sayısı
        #  göz sınıflandırmasında daha büyük değer kullanılır hata azaltma için
        #  minSize: minumu pencere büyüklüğü
        eyeRects = e.detectMultiScale(faceROI, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex, ey, ew, eh) in eyeRects:
            rects.append((fx+ex, fy+ey, fx+ex+ew, fy+ey+eh))
    return rects

#  açılan kamera penceresinin boyutunu belirleme
def wSize(width, frame):
    (h, w) = frame.shape[:2]
    r = width / float(w)
    return width, int(h*r)

#
def main():
    #  ek seçenek olarak dışardan video dosyasını ekleme
    arg = argparse.ArgumentParser()
    arg.add_argument("-v", "--video", help="path to the video file")
    args = vars(arg.parse_args())

    e = addCascade()
    # dışardan video dosyası verilip verilmediğinin kontrolü
    if not args.get("video", False):
        camera = cv2.VideoCapture(0)
    else:
        camera = cv2.VideoCapture(args["video"])

    while True:
        #  kameredan yada videodan görüntülerin frame olarak alınması
        #  grabbed: frame in alınıp alınmadığı bilgisini tutar(True/False)
        (grabbed, frame) = camera.read()
        #  videonun sonunna gelinmesinin kontrol edilmesi
        if args.get("video") and not grabbed:
            break

        width, height = wSize(600, frame)
        #  çerçevenin yeniden boyutlandırılması
        frame = cv2.resize(frame, (width, height))
        #  görünütünün griye çevrilmesi, tek boyutta
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #  yüz ve göz çevrelerinin bulunması
        rects = track(gray, e)
        #  döngü ile bulunan yüzlerin ve gözlerin etrafını çizdirme
        for rect in rects:
            cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

        cv2.imshow("Yuz ve Goz Takibi", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
