from django import forms
from django.forms import ModelForm
from .models import CropAdv
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CropAdv, ImageFormModel
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

for c in SEASON_CONTENT:
    print(c);

MYCONST = list(SEASON_CONTENT);

# EASON_CONTENT = list((k, v) for k, v in mySeasonTypeDict.items())

class BasicForm(forms.Form):
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
    season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))
    
class AdvanceForm(ModelForm):
    class Meta:
        model = CropAdv
        fields = ('name', 'season', 'soil', 'max_temp', 'min_temp', 'max_humidity', 'min_humidity', 'max_pH', 'min_pH',)
        
    # widgets = {
    name = forms.CharField(label="Name")
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices= SOIL_CONTENT))
    season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))

    temp_min = forms.FloatField()
    temp_max = forms.FloatField()
    humidity_min = forms.FloatField()
    humidity_max = forms.FloatField()
    ph_min = forms.FloatField()
    ph_max = forms.FloatField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"class": "form-control"})
        # or iterate over field to add class for each field
        # for field in self.fields:
        #     self.fields[field].widget.attrs.update({'class':"form-control"})

class ImageForm(forms.Form):
    Plant_Image = forms.ImageField()

class ImageForm(ModelForm):
    name = forms.CharField(label="Testing char Name", max_length=30, required=False)
    image = forms.ImageField(required=False)
    
    class Meta:
        model = ImageFormModel
        fields = ["name", "image"]