import pyqrcode as pyqr

qr = pyqr.create("Ornek QRCode")

qr.png("qrcode.png", scale=15)

print("Done.")
