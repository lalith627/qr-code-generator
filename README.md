📌 QR Code Generator for DSA Syllabus Link
This repository contains two simple Python scripts that generate QR codes for a DSA (Data Structures & Algorithms) syllabus link hosted on Whimsical. One script creates a basic QR code, while the other adds customization like color and error correction.

🗂 Files
simple_qr.py
Generates a basic black-and-white QR code using the qrcode library.

python
Copy
Edit
import qrcode as qr
img = qr.make("https://whimsical.com/complete-dsa-syllabus-home-FsbU9GBpipqWCphtYAUYV1")
img.save("dsa-syllabus.png")
📤 Output: dsa-syllabus.png

custom_qr.py
Generates a customized QR code with:

Higher error correction level

Colored foreground and background

Configurable size and border

python
Copy
Edit
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

img = qr.make_image(fill_color="red", back_color="black")
img.save("dsa2-syllabus.png")
📤 Output: dsa2-syllabus.png

📦 Requirements
Install dependencies with:

nginx
Copy
Edit
pip install qrcode pillow
🚀 How to Run
Run either file in your terminal:

nginx
Copy
Edit
python simple_qr.py
# or
python custom_qr.py
📷 Preview
You can scan the output images to instantly access the DSA syllabus page.

🛠️ Author
Created with ❤️ for learning and contributing daily.

🌟 Star this repo if it helped you!
