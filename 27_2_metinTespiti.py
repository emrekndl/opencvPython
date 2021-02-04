import cv2
import  pytesseract
from captureScreen import captureScreen

camera = captureScreen()

while  True:
    img = camera.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    for  i in boxes.splitlines():
        i = i.split()
        #  print(i)
        x, y, w, h = int(i[1]), int(i[2]), int(i[3]), int(i[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 255, 0), 2)
        cv2.putText(img, i[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (50, 50, 255), 2)
    cv2.imshow("sonuc", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

