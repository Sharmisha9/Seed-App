from django import forms
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
    
class AdvanceForm(forms.Form):
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
    season = forms.CharField(label="Choose a season", widget = forms.Select(choices=SEASON_CONTENT))
    temperature = forms.FloatField(label="Sensor temperature value", widget = forms.TextInput)
    humidity = forms.FloatField(label="Sensor humidity value", widget = forms.TextInput)
    pH = forms.FloatField(label="Sensor pH value", widget = forms.TextInput)
        
# class MyForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=30)
#     last_name = forms.CharField(label="Last Name", max_length=30)
#     email = forms.EmailField(label="Email", max_length=100, required=False)
#     phone = forms.CharField(label="Phone")
