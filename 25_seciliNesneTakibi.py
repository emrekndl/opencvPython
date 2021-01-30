import cv2


camera = cv2.VideoCapture(0)

#  takip fonksiyonları
# hızlı
#tracker = cv2.TrackerMOSSE_create()
# yavaş, daha doğru
tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerTLD_create()

#  kamerdan ilk görüntü(frame) alınıp, alanın(roi) seçilmesi
grabbed, frame = camera.read()

boundingBox = cv2.selectROI("Takip", frame, False)
tracker.init(frame, boundingBox)

#  seçili alanın etrafını çizme fonksiyonu
def drawBox(img, bbox):
    #  seçili alan konumu
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    #  kare ve yazı konulması
    cv2.rectangle(img, (x, y), ((x +w), (y + h)), (255, 0, 255), 3, 1)
    cv2.putText(frame, "Takip Ediliyor", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

while True:
    timer = cv2.getTickCount()
    grabbed, frame = camera.read()

    #  seçili alanın takip fonksiyonunda güncellenemsi
    grabbed, boundingBox = tracker.update(frame)
    #print(boundingBox)
    if grabbed:
        drawBox(frame, boundingBox)
    else:
        cv2.putText(frame, "Nesne Bulunamadi!", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    #  fps hesaplama
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    #  fps i ekranda yazma
    cv2.putText(frame, "FPS: " + str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Takip", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
