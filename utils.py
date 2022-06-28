import os
from PIL import Image
import shutil
import unet
import zipfile

output_airway_folder = 'output_airway'
output_tongue_folder = 'output_tongue'
output_velum_folder = 'output_velum'
output_folders = [output_airway_folder,output_tongue_folder,output_velum_folder]

def load_image(image_file):
    img = Image.open(image_file)
    return img

'''
def compress_data():
    if os.path.exists('output_airway.zip'):
        os.remove('output_airway.zip')
    if os.path.exists('output_tongue.zip'):
        os.remove('output_tongue.zip')
    if os.path.exists('output_velum.zip'):
        os.remove('output_velum.zip')
    shutil.make_archive('output_airway','zip','./output_airway')
    shutil.make_archive('output_tongue','zip','./output_tongue')
    shutil.make_archive('output_velum','zip','./output_velum')
    #shutil.make_archive('')
    print('data compressed')
    '''



def compress_data(folders, zip_filename):
    os.remove('output.zip')
    zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

    for folder in folders:
        print(folder)
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                zip_file.write(
                    os.path.join(dirpath, filename),
                    os.path.relpath(os.path.join(dirpath, filename), os.path.join(folders[0], '../..')))

    zip_file.close()    

def read_the_folder(folder):
    isExistA = os.path.exists(output_airway_folder)
    isExistT = os.path.exists(output_tongue_folder)
    isExistV = os.path.exists(output_velum_folder)
    if not isExistA:
        os.makedirs(output_airway_folder)
    if not isExistT:
        os.makedirs(output_tongue_folder)
    if not isExistV:
        os.makedirs(output_velum_folder)
    print('folder making sucessful')
    unet.unet_model()