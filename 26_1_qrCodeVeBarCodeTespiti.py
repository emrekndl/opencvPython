import  cv2
import  numpy as np
from pyzbar.pyzbar import decode
from captureScreen import captureScreen

#  img = cv2.imread("images/qrcode_r.png")

#  görüntü kaynağını ekrandan alma
#  camera2 = captureScreen()

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

while True:

    grabbed, frame = camera.read()

    #  frame = camera2.read()

    #  qrcode ve barcode görüntülerin verilerini alma
    #  dcode.data, içerdiği mesaj(byte), dcode.rect, dcode un alanı(köşe noktaları)
    for dcode in decode(frame):
        #  byte veriyi stringe çevirme
        myData = dcode.data.decode('utf-8')
        print(myData)
        #  polygon, düzgün şekilleri olmayan(çevrilmiş) görüntülerin alanını verir
        pointsPolygon = np.array([dcode.polygon], np.int32)
        pointsPolygon = pointsPolygon.reshape((-1, 1, 2))

        cv2.polylines(frame, [pointsPolygon], True, (255, 0, 255), 5)
        #  metinin de çevrilmemesi için rect(dikdörtgen) çevresinin verilmesi
        pointsText = dcode.rect
        cv2.putText(frame, myData, (pointsText[0], pointsText[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow("sonuc", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
