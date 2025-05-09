import qrcode as qr
img = qr.make("https://whimsical.com/complete-dsa-syllabus-home-FsbU9GBpipqWCphtYAUYV1")

img.save("dsa-syllabus.png")