import os
from PIL import Image
import shutil

def load_image(image_file):
    img = Image.open(image_file)
    return img

def compress_data():
    os.remove('output.zip')
    shutil.make_archive('output','zip','./output')
    print('data compressed')