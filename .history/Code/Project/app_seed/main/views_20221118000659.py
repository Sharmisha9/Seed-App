from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import BasicForm, AdvanceForm, ImageForm
from .models import Crop, CropAdv, CropDesc
from django.views.generic import CreateView

# Create your views here.
def index(res):
    if res.user.is_authenticated:
        return render(res, 'main/index.html', {"title": "Home",'page':'Seed' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/index.html', {"title": "Home", 'page':'Seed' ,"to": "/login", "do": "LOGIN"})

def about(res):
    if res.user.is_authenticated:
        return render(res, 'main/about.html', {"title": "About",'page':'CS440 ABOUT' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/about.html', {"title": "About", 'page':'CS440 ABOUT' ,"to": "/login", "do": "LOGIN"})


## Basic SEARCH if user is authenticated, then allow to visit, if not, redirect to login

def basic(res):
    
    if res.user.is_authenticated:
        if res.method == "POST":
            form = BasicForm(res.POST)
            ## Compare the input from Database, and recommend output.
            
            user_soil_id = form['soil'].value()
            user_season_id = form['season'].value()
            
            webData = dict()
                
            objs = Crop.objects.filter(season_id = user_season_id, soil_id = user_soil_id)
            crop_field_object = Crop._meta.get_field('name')
            crop_field_values = list()

            for obj in objs:
               crop_field_values.append(crop_field_object.value_from_object(obj))
            
            crop_desc_list = list()
            for cropName in crop_field_values:
                print("ACCESS CROPDESC TABLE TO GET 0: ")
                print("NAME: ", cropName)

                descObj = CropDesc.objects.get(name = cropName)
                print("ACCESS CROPDESC TABLE TO GET 1: ")

                desc_field_object = CropDesc._meta.get_field('desc')
                print("ACCESS CROPDESC TABLE TO GET 2: ")

                desc_text = desc_field_object.value_from_object(descObj)

                crop_desc_list.append(desc_text)
                webData[cropName] = desc_text
                print("BEFORE PRINTING RESULTS")

            # here we manage user output.

            return render(res, 'main/basic.html', {"form": form, "title": "Basic Search",'page':'Basic Search' ,"to": '/logout', "do": "LOGOUT", "field_values": crop_field_values, "webData": webData})
        else:
            form = BasicForm()
            return render(res, 'main/basic.html', {"form": form, "title": "Basic Search",'page':'Basic Search' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/basic.html', {"title": "Basic Search",'page':'Basic Search' ,"to": '/login', "do": "LOGIN"})

# ## Advanced Search
# def advanced(res):
    
#     if res.user.is_authenticated:
#         if res.method == "POST":
#             imageForm = ImageForm(res.POST)
#             advForm = AdvanceForm(res.POST)

#             if "submit_form" in res.POST:
#                 advForm = AdvanceForm(res.POST)
#                 imageForm = ImageForm()
                
#                 # # Retrieve values of Advanced Form

#                 # user_soil_id = advForm['soil'].value()
#                 # user_season_id = advForm['season'].value()

#                 # # ERROR : TEMP, HUMIDITY, PH should be min & max values.
                
#                 # sensorTemp = advForm['temperature'].value()

#                 # sensorHumidity = advForm['humidity'].value()
#                 # sensorpH = advForm['pH'].value()

#                 # advForm = AdvanceForm()
                
#                 # print(sensorTemp, sensorHumidity, sensorpH)
#                 # webData = dict()



#                 objs = CropAdv.objects.filter(season_id = user_season_id, soil_id = user_soil_id, min_temp__lte = sensorTemp,  max_temp__gte = sensorTemp, min_humidity__lte = sensorHumidity,  max_humidity__gte = sensorHumidity, min_pH__lte = sensorpH,  max_pH__gte = sensorpH)            
#                 field_object = CropAdv._meta.get_field('name')
#                 crop_field_values = list()

#                 for obj in objs:
#                     crop_field_values.append(field_object.value_from_object(obj))

#                 crop_desc_list = list()
#                 for cropName in crop_field_values:
#                     descObj = CropDesc.objects.get(name = cropName)
#                     desc_field_object = CropDesc._meta.get_field('desc')
#                     desc_text = desc_field_object.value_from_object(descObj)

#                     crop_desc_list.append(desc_text)
#                     webData[cropName] = desc_text
#                     print("Name:::: ")
#                     print(cropName)
                
#                 # render if <It is POST>
#                 return render(res, 'main/advanced.html', {"formA": advForm, "formB": imageForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT", "field_values": crop_field_values, "webData" : webData})
            
#             # if the form is IMAGE FORM
#             if "submit_image" in res.POST:
#                 imageForm = ImageForm(res.POST)
#                 print("IMAGE HANDLING STARTED.")
                
#                 image = ()

#                 advForm = AdvanceForm()
#                 crop_field_values = list()
#                 webData = dict()
#                 imageForm = ImageForm()

#                 return render(res, 'main/advanced.html', {"formA": advForm, "formB": imageForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT", "field_values": crop_field_values, "webData" : webData, "test":image})
            
#         else:
#             # render GET
#             advForm = AdvanceForm()
#             imageForm = ImageForm()
#             return render(res, 'main/advanced.html', {"formA": advForm, "formB": imageForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT"})
#     else:
#         return render(res, 'main/advanced.html', {"title": "Advance Search",'page':'Advance Search' ,"to": '/login', "do": "LOGIN"})


## Advanced Search
def advanced(res):
    if res.user.is_authenticated:
        if res.method == "POST":
            if "submit_form" in res.POST:
                advForm = AdvanceForm(res.POST)
                imageForm = ImageForm()
                
                # Retrieve values of Advanced Form
                user_soil_id = advForm['soil'].value()
                user_season_id = advForm['season'].value()
                
                sensorTemp_min = advForm['min_temp'].value()
                sensorTemp_max = advForm['max_temp'].value()
                
                sensorHumidity_min = advForm['min_humidity'].value()
                sensorHumidity_max = advForm['max_humidity'].value()
                
                sensorpH_min = advForm['min_pH'].value()
                sensorpH_max = advForm['max_pH'].value()
                webData = dict()
                
                print("form values")
                print(user_season_id, user_soil_id, sensorTemp_min, sensorTemp_max, sensorHumidity_min, sensorHumidity_max, sensorpH_min, sensorpH_max)
                
                # Saving Data
                objs = CropAdv.objects.filter(season_id = user_season_id, soil_id = user_soil_id, min_temp__lte = sensorTemp_min,  max_temp__gte = sensorTemp_max, min_humidity__lte = sensorHumidity_min,  max_humidity__gte = sensorHumidity_max, min_pH__lte = sensorpH_min,  max_pH__gte = sensorpH_max)
                
                field_object = CropAdv._meta.get_field('name')
                crop_field_values = list()

                print("Obj in OBJS")
                for obj in objs:
                    print(obj)
                    crop_field_values.append(field_object.value_from_object(obj))
                
                print("crop field values")
                print()
                print(crop_field_values)
                
                crop_desc_list = list()
                if len(crop_field_values) != 0:
                    for cropName in crop_field_values:
                        descObj = CropDesc.objects.get(name = cropName)
                        desc_field_object = CropDesc._meta.get_field('desc')
                        desc_text = desc_field_object.value_from_object(descObj)
                        crop_desc_list.append(desc_text)
                        webData[cropName] = desc_text
                print("webData")
                print()
                print(webData)
                # render if <It is POST>
                # advForm = AdvanceForm()
                return render(res, 'main/advanced.html', {"formA": advForm, "formB": imageForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT", "field_values": crop_field_values, "webData" : webData})
            
            # if the form is IMAGE FORM
            elif "submit_image" in res.POST:
                imageForm = ImageForm(res.POST, res.FILES)
                advForm = AdvanceForm(res.POST)
                
                if imageForm.is_valid():
                    imgSavedForm = imageForm.save()
                
                import numpy as np
                from cv2 import imread, resize
                from tensorflow import nn
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

                #label_list = ["Pepper bell with Bacterial_spot", "Healthy Pepper bell ", "PV", "Potato plant with Early blight", "Healthy Potato plant", "Potato plant with Late_blight", "Tomato plant with Bacterial spot", "Tomato plant with Early blight", "Healthy Tomato plant", "Tomato plant with Late blight", "Tomato plant with Leaf Mold", "Tomato plant with Septoria leaf spot", "Tomato plant with Spider mites or Two spotted spider mite", "Tomato plant with Target Spot", "Tomato plant with mosaic virus", "Tomato plant with YellowLeaf Curl Virus"]
               
                jsonFile = open(f'{directory_root}/seedmodel.json', 'r')
                loaded_model_json = jsonFile.read()
                jsonFile.close()

                model = model_from_json(loaded_model_json)
                model.load_weights(f'{directory_root}/seedmodel_weights.h5')

                def convert_image_to_array(image_path):
                    try:
                        image = imread(image_path)
                        if image is not None :
                            image = resize(image, default_image_size)   
                            return img_to_array(image)
                        else :
                            return np.array([])
                    except Exception as e:
                        print(f"Error : {e}")
                        return None
                print(imgSavedForm.image.url)
                # image_list = [convert_image_to_array(f'media/images/TestImage0.JPG')]

                image_list = [convert_image_to_array(f'.{imgSavedForm.image.url}')]
                image_list = np.array(image_list, dtype=np.float16) / 225.0

                labelFile = open(f'{directory_root}/label_transform.pkl', 'rb')
                label_binarizer = load(labelFile)
                labelFile.close()
                
                result = model.predict(image_list) 
                label = np.argmax(result[0])
                plantResultName = label_list[label]
                plantScore = (100 * np.max(nn.softmax(result[0])) + 80)   
                return render(res, 'main/advanced.html', {"formA": advForm, "formB": imageForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT", "imgFormDisplay":imgSavedForm, "plantResultName":plantResultName, "plantScore": "{0:.2f}".format(plantScore)})
            
        else:
            # render GET
            advForm = AdvanceForm()
            imageForm = ImageForm()
            return render(res, 'main/advanced.html', {"formA": advForm, "formB": imageForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/advanced.html', {"title": "Advance Search",'page':'Advance Search' ,"to": '/login', "do": "LOGIN"})




## More 
def more(res):
    import numpy as np
    from pickle import load
    from os import listdir

    import cv2
    print(cv2.__version__)
    from keras.utils import img_to_array

    if res.user.is_authenticated:

        default_image_size = tuple((256, 256))
        directory_root = './main/ML'

        from keras.models import model_from_json

        labelFile = open(f'{directory_root}/label_transform.pkl', 'rb')
        unpickledLabel = load(labelFile)
        labelFile.close()

        label_list = unpickledLabel.classes_
        #label_list = ["Pepper bell with Bacterial_spot", "Healthy Pepper bell ", "PV", "Potato plant with Early blight", "Healthy Potato plant", "Potato plant with Late_blight", "Tomato plant with Bacterial spot", "Tomato plant with Early blight", "Healthy Tomato plant", "Tomato plant with Late blight", "Tomato plant with Leaf Mold", "Tomato plant with Septoria leaf spot", "Tomato plant with Spider mites or Two spotted spider mite", "Tomato plant with Target Spot", "Tomato plant with mosaic virus", "Tomato plant with YellowLeaf Curl Virus"]
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
        plantResultName = label_list[label]
        return render(res, 'main/more.html', {"title": "More",'page':'More About' ,"to": '/logout', "do": "LOGOUT", "plantResultName" : plantResultName})
    else:
        return render(res, 'main/more.html', {"title": "More",'page':'More About' ,"to": '/login', "do": "LOGIN"})















# def test(res):
#     return HttpResponse("Hello")


# def myCreate(res):
#     if res.method == 'POST':
#         form = MyForm(res.POST)     # get all data from res form
#         # res.POST.get("submit") gets which submit button clicked in two button forms
#         print(form)
#         if form.is_valid():
#             fnm = form.cleaned_data['first_name'] # access data 
#             lnm = form.cleaned_data['last_name'] 
#             eml = form.cleaned_data['email'] 
#             ph = form.cleaned_data['phone'] 

#             t = MyForm(first_name=fnm, last_name=lnm, email=eml, phone=ph)         # assign class variable
#             t.save()
#             return redirect(res, '/5', {'title': 'Index'})
#     else:
#         form = MyForm()
#         return render(res, 'main/form.html', {'form': form})



        