from django import forms
from django.forms import ModelForm
from .models import CropAdv
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

class BasicForm(forms.Form):
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
    season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))
    
class AdvanceForm(ModelForm):
    class Meta:
        model = CropAdv
        fields = ('name', 'season', 'soil', 'max_temp', 'min_temp', 'max_humidity', 'min_humidity', 'max_pH', 'min_pH',)
        
        # widgets = {
        name = forms.CharField(label="Name")
        soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
        season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))

        temp_min = forms.FloatField()
        temp_max = forms.FloatField()
        humidity_min = forms.FloatField()
        humidity_max = forms.FloatField()
        ph_min = forms.FloatField()
        ph_max = forms.FloatField()

        # fields = ('season',)



    # soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
    # season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))
    # # temperature = forms.FloatField(label="Sensor temperature value", widget = forms.TextInput)
    # # humidity = forms.FloatField(label="Sensor humidity value", widget = forms.TextInput)
    # # pH = forms.FloatField(label="Sensor pH value", widget = forms.TextInput)
        

    # temp_min = forms.FloatField(label="Minimum Temperature");
    # temp_max = forms.FloatField(label="Maximum Temperature");
    # humidity_min = forms.FloatField(label="Minimum Humidity");
    # humidity_max = forms.FloatField(label="Maximum Humidity");
    # ph_min = forms.FloatField(label="Minimum pH");
    # ph_max = forms.FloatField(label="Maximum pH");

class ImageForm(forms.Form):
    Plant_Image = forms.ImageField()

