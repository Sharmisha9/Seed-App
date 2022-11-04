import numpy as np
import cv2
from keras.utils import img_to_array
from pickle import load
from os import listdir

default_image_size = tuple((256, 256))
directory_root = './main/ML'

from keras.models import model_from_json

labelFile = open(f'{directory_root}/label_transform.pkl', 'rb')
unpickledLabel = load(labelFile)
labelFile.close()

label_list = unpickledLabel.classes_

jsonFile = open(f'{directory_root}/seedmodel.json', 'r')
loaded_model_json = jsonFile.read()
jsonFile.close()

model = model_from_json(loaded_model_json)
model.load_weights(f'{directory_root}/seedmodel_weights.h5')

def convert_image_to_array(image_path):
    try:
        image = cv2.imread(image_path)
        if image is not None :
            image = cv2.resize(image, default_image_size)   
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None
testImg = 'healthy_potato.JPG'
image_list = [convert_image_to_array(f'{directory_root}/{testImg}')]
image_list = np.array(image_list, dtype=np.float16) / 225.0

labelFile = open(f'{directory_root}/label_transform.pkl', 'rb')
label_binarizer = load(labelFile)
labelFile.close()

result = model.predict(image_list) 
label = np.argmax(result[0])
print(label_list[label])