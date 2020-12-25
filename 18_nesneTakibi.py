import argparse
import cv2
import numpy as np
import time


def main():
    #  renk aralığı belirleme *mavi
    lower_blue = np.array([100, 67, 0], dtype="uint8")
    upper_blue = np.array([255, 128, 50], dtype="uint8")
    #lower_green = np.array([60, 100, 50], dtype="uint8")
    #upper_green = np.array([60, 255, 255], dtype="uint8")
    #s = 15 # sensitivity = 15
    #lower_green = np.array([60-s, 100, 55], dtype="uint8")
    #upper_green = np.array([60+s, 255, 255], dtype="uint8")

    #  dışardan video dosyası verilmesi
    arg = argparse.ArgumentParser()
    arg.add_argument("-v", "--video", help="path to the video file")
    args = vars(arg.parse_args())

    #   dışardan video dosyası verilip verilmediğinin kontrolü
    if not args.get("video", False):
        camera = cv2.VideoCapture(0)
    else:
        camera = cv2.VideoCapture(args["video"])

    dim = (600, 450) # pencere boyutu
    while True:
        #  kameredan yada videodan görüntülerin frame olarak alınması
        #  grabbed: frame in alınıp alınmadığı bilgisini tutar(True/False)
        (grabbed, frame) = camera.read()
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA) # pencre boyutunun ayarlanması
        #  videonun sonunna gelinmesinin kontrol edilmesi
        if args.get("video") and not grabbed:
            break
        #  çerçevedeki(frame) mavi tonu bulmak için(çerçeve, alt eşik, üst eşik)
        #  üst ve alt aralığa düşen pikseller beyaz, diğerlerinin siyah olarak ayarlanmasını sağlar
        blue = cv2.inRange(frame, lower_blue, upper_blue)
        #  parazitleri kaldırmak için bulanıklık uygulanır
        blue = cv2.GaussianBlur(blue, (3, 3), 0)
        #  findContours görüntüyü bozduğu için görüntünün kopyası alınır
        #  görüntü, görüntünün dış çevresi alma, görüntünün köşegen dikey  yatay segmentlerini şıkıştırıp bileştirir
        (cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #  şekil çevresi(contours) bulduğunun kontrolü
        if len(cnts) > 0:
            #  contourArea şekil çevresi alanı bulmak için kullanılır
            #  şekil çevreleri ters sırayla(önce en büyük) sıralanır, ilk sıradaki en bulunan en büyük şekildir
            cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
            #  Cv2.minAreaRect, şekil çevresi etrafındaki minimum sınırlayıcı kutuyu hesaplar
            #  cv2.boxPoints, sınırlayıcı şekli bir nokta listesi olacak şekilde yeniden şekillendirir
            rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
            #  çevresini çizdirme
            #  görüntü, çevre sayısı, -1 hepsini çizdirme(sadece biri için 2,3,4,5), çizdirme rengi, kalınlık
            cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

        cv2.imshow("Nesne Takibi", frame)
        cv2.imshow("Binary", blue)
        time.sleep(0.025)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # kameranın kapatılması
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
