import utils
import os
import unet

from tensorflow.keras.applications import mobilenet
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
vgg_model = mobilenet.MobileNet(weights='imagenet')

output_folder = 'output'

#//  - connect all the segmentation models
#def Imagenet(img):
    #numpy_image = img_to_array(img)
    #image_batch = np.expand_dims(numpy_image, axis=0)
    #processed_image = mobilenet.preprocess_input(image_batch.copy())
    #predictions = vgg_model.predict(processed_image)
    #label_vgg = decode_predictions(predictions)
#    return img


def read_the_folder(folder):
    isExist = os.path.exists(output_folder)
    if not isExist:
        os.makedirs(output_folder)
    unet.unet_model()


''''
    images = []
    for filename in os.listdir(folder):
        img = utils.load_image(os.path.join(folder, filename))
        if img is not None:
            #output = Imagenet(img)
            unet.unet_model()
            isExist = os.path.exists(output_folder)
            if not isExist:
                os.makedirs(output_folder)
            #output.save(os.path.join(output_folder,filename))
'''
