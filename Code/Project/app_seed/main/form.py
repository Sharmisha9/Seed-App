from django import forms

## for user input form for Basic Search
SOIL_CONTENT = (
    ('hcsl', "Heavy lcay and silt loam"),
    ('sl', "Sandy loam"),
    ('ls', "Loam soils"),
    ('wdls', "Well drained loamy soil"),
    ('bcs',"Black cotton soils"),
    ('dss', "Dry sandy soil"),
    ('sls', "Sandy loam soils"),
    ('shcs', "Sandy to heavy cotton soils"),
    ('dsl', "Deep, sandy laoms"),
    ('dls', "Deep loamy soils"),
    ('avs', "Alluvial and volcanic soils"),
    ('lslrc', "Light sandy loams to red clay"),
    ('gas', "Grey alluvial soils"),
    ('fvrd', "Fetile volcanic red earch"),
)

SEASON_CONTENT=(
    ('spring', "Spring"),
    ('summer', "Summer"),
    ('fall', "Fall"),
    ('winter', "Winter"),
)
class BasicForm(forms.Form):
    soil = forms.CharField(label="Choose a Soil type", widget = forms.Select(choices=SOIL_CONTENT))
    season = forms.CharField(label="Choose a seaon", widget = forms.Select(choices=SEASON_CONTENT))





# class MyForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=30)
#     last_name = forms.CharField(label="Last Name", max_length=30)
#     email = forms.EmailField(label="Email", max_length=100, required=False)
#     phone = forms.CharField(label="Phone")
