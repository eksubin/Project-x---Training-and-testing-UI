from tabnanny import verbose
from tensorflow.keras.models import load_model
import numpy as np
import os
import skimage.io as io
import skimage.transform as trans

Sky = [128,128,128]
Building = [128,0,0]
Pole = [192,192,128]
Road = [128,64,128]
Pavement = [60,40,222]
Tree = [128,128,0]
SignSymbol = [192,128,128]
Fence = [64,64,128]
Car = [64,0,128]
Pedestrian = [64,64,0]
Bicyclist = [0,128,192]
Unlabelled = [0,0,0]
COLOR_DICT = np.array([Sky, Building, Pole, Road, Pavement,
                          Tree, SignSymbol, Fence, Car, Pedestrian, Bicyclist, Unlabelled])

model_locA = './airway.hdf5'
model_locT = './tongue.hdf5'
model_locV = './velum.hdf5'
test_loc = './test_images'
output_locA = './output_airway'
output_locT = './output_tongue'
output_locV = './output_velum'

modelA = load_model(model_locA)
modelT = load_model(model_locT)
modelV = load_model(model_locV)

def testGenerator(test_path,start_img_num,end_img_num,target_size = (256,256),flag_multi_class = False,as_gray = True):
    for i in range(start_img_num,end_img_num):
        img = io.imread(os.path.join(test_path,"%d.png"%i),as_gray = as_gray)
        img = img / 255
        img = trans.resize(img,target_size)
        img = np.reshape(img,img.shape+(1,)) if (not flag_multi_class) else img
        img = np.reshape(img,(1,)+img.shape)
        yield img

def labelVisualize(num_class,color_dict,img):
    img = img[:,:,0] if len(img.shape) == 3 else img
    img_out = np.zeros(img.shape + (3,))
    for i in range(num_class):
        img_out[img == i,:] = color_dict[i]
    return img_out / 255

def saveResult(save_path,npyfile,flag_multi_class = False,num_class = 2):
    for i,item in enumerate(npyfile):
        img = labelVisualize(num_class,COLOR_DICT,item) if flag_multi_class else item[:,:,0]
        io.imsave(os.path.join(save_path,"%d.png"%i),img)

#def filenames(folder):
#    for filename in os.listdir(folder):

def unet_model():
    test_generatorA = testGenerator(test_loc,0,5,target_size=(256,256))
    test_generatorT = testGenerator(test_loc,0,5,target_size=(256,256))
    test_generatorV = testGenerator(test_loc,0,5,target_size=(256,256))
    outputA = modelA.predict_generator(test_generatorA,5,verbose=1)
    outputT = modelT.predict_generator(test_generatorT,5,verbose=1)
    outputV = modelV.predict_generator(test_generatorV,5,verbose=1)
    saveResult(output_locA,outputA)
    saveResult(output_locT,outputT)
    saveResult(output_locV,outputV)