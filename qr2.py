import qrcode as qr
from PIL import Image


qr = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://whimsical.com/complete-dsa-syllabus-home-FsbU9GBpipqWCphtYAUYV1")
qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="black")
img.save("dsa2-syllabus.png")
