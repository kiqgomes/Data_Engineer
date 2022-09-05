# pip install -q pyqrcode
# pip install -q pillow
# pip install -q pypng
from importlib.resources import path
from pathlib import Path

import pyqrcode
from PIL import Image

to_qrcode = input("Type anything: ")
qr_code = pyqrcode.create(to_qrcode)
path = Path.cwd()

qr_code.png(f"{path}/QRCode.png",scale=5)
Image.open(f"{path}/QRCode.png")
