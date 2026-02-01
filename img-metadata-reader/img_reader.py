from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

print('Enter image file name (must be in the same directory)\nexample: img.jpg')
img_path = Path(__file__).with_name(input('>'))
img = Image.open(img_path)

exif = img._getexif()

def meta_data(img):
    data = img._getexif()
    if data:
        for k, v in data.items():
            tag = TAGS.get(k, k)
            print(f'{tag:25}: {v}')
    else:
        print('NO STANDARD EXIF DATA')
        for k, v in img.info.items():
            print(k,v)
    
meta_data(img)