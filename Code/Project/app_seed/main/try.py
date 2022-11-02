import numpy as np
import cv2
from keras.utils import img_to_array
from pickle import load
from os import listdir

default_image_size = tuple((256, 256))
directory_root = 'C:/UIC EDUCATION/CS440 SE/Coding Project/SEED/440-Group-24-Fall-2022/Code/Project/app_seed/main/ML'

from keras.models import model_from_json

label_list = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'PlantVillage', 'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_healthy', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 'Tomato__Tomato_mosaic_virus', 'Tomato__Tomato_YellowLeaf__Curl_Virus']
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

image_list = [convert_image_to_array(f'{directory_root}/TestImage4.JPG')]
image_list = np.array(image_list, dtype=np.float16) / 225.0

labelFile = open(f'{directory_root}/label_transform.pkl', 'rb')
label_binarizer = load(labelFile)
labelFile.close()

result = model.predict(image_list) 
label = np.argmax(result[0])
print(label_list[label])