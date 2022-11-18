from django import forms
from django.forms import Form, ModelForm
from .models import CropAdv, ImageFormModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import csv

mySoilTypeDict = dict()
with open("Soil.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
         mySoilTypeDict[row[0]] = row[1]

mySeasonTypeDict = dict()
with open("Season.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
         mySeasonTypeDict[row[0]] = row[1]
         
## for user input form for Basic Search
SOIL_CONTENT = tuple((k, v) for k, v in mySoilTypeDict.items())

SEASON_CONTENT = tuple((k, v) for k, v in mySeasonTypeDict.items())

class BasicForm(Form):
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
    season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))
    
# class AdvanceForm(forms.Form):
#     soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT), required=False)
#     season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT), required=False)
#     temperature = forms.FloatField(label="Sensor temperature value", widget = forms.TextInput, required=False)
#     humidity = forms.FloatField(label="Sensor humidity value", widget = forms.TextInput, required=False)
#     pH = forms.FloatField(label="Sensor pH value", widget = forms.TextInput, required=False)

class AdvanceForm(ModelForm):
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices= SOIL_CONTENT))
    season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))
    min_temp = forms.FloatField(min_value=-50)
    max_temp = forms.FloatField(max_value=60)
    min_humidity = forms.FloatField(min_value=0)
    max_humidity = forms.FloatField(max_value=100)
    min_pH = forms.FloatField(min_value=0)
    max_pH = forms.FloatField(max_value=14)
    
    class Meta:
        model = CropAdv
        fields = ["max_temp","min_temp","max_humidity", "min_humidity", "max_pH", "min_pH"]
    

class ImageForm(ModelForm):
    name = forms.CharField(label="Testing char Name", max_length=30, required=False)
    image = forms.ImageField(required=False)
    
    class Meta:
        model = ImageFormModel
        fields = ["name", "image"]