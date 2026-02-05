import pytesseract as tess
from PIL import Image
import sys

source_file = sys.argv[1]
target_file = sys.argv[2]

with Image.open(source_file) as image:
    txt = tess.image_to_string(image)

with open(target_file, 'w') as target:
    target.write(txt)
