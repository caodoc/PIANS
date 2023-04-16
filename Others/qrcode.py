import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
                
# Create a QR code
qr = pyqrcode.create("Tri ngu nhu con bo")
qr.png("test.png", scale=9)
               
# Read a QR code
d = decode(Image.open("qrcode.png"))