from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

print('Enter image file name (must be in the same directory)\nexample: img.jpg')
img_path = Path(__file__).with_name(input('>'))
img = Image.open(img_path)

exif = img._getexif()

if exif:
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f'{tag:25}: {value}')
else: 
    print('no exif data')