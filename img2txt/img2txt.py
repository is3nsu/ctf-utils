import pytesseract as tess
from PIL import Image
from pathlib import Path
import sys


img_path = Path(__file__).with_name(f'{sys.argv[1]}')
img = Image.open(img_path)
txt = tess.image_to_string(img)
print(txt)
