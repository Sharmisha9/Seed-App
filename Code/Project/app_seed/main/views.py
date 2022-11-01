from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import BasicForm, AdvanceForm
from .models import Crop, CropAdv

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
    
            field_name = 'name'
            objs = Crop.objects.filter(season_id = user_season_id, soil_id = user_soil_id)
            field_object = Crop._meta.get_field(field_name)
            field_values = list()
            
            for obj in objs:
               field_values.append(field_object.value_from_object(obj))
            
            return render(res, 'main/basic.html', {"form": form, "title": "Basic Search",'page':'Basic Search' ,"to": '/logout', "do": "LOGOUT", "field_values": field_values})
        else:
            form = BasicForm()
            return render(res, 'main/basic.html', {"form": form, "title": "Basic Search",'page':'Basic Search' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/basic.html', {"title": "Basic Search",'page':'Basic Search' ,"to": '/login', "do": "LOGIN"})

## Advanced Search
def advanced(res):
    if res.user.is_authenticated:
        if res.method == "POST":
            advForm = AdvanceForm(res.POST)
            
            user_soil_id = advForm['soil'].value()
            user_season_id = advForm['season'].value()
            sensorTemp = advForm['temperature'].value()
            sensorHumidity = advForm['humidity'].value()
            sensorpH = advForm['pH'].value()
            
            print(sensorTemp, sensorHumidity, sensorpH)
            
            field_name = 'name'
            objs = CropAdv.objects.filter(season_id = user_season_id, soil_id = user_soil_id, min_temp__lte = sensorTemp,  max_temp__gte = sensorTemp, min_humidity__lte = sensorHumidity,  max_humidity__gte = sensorHumidity, min_pH__lte = sensorpH,  max_pH__gte = sensorpH)            
            field_object = CropAdv._meta.get_field(field_name)
            field_values = list()
            
            for obj in objs:
               field_values.append(field_object.value_from_object(obj))
            
            return render(res, 'main/advanced.html', {"form": advForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT", "field_values": field_values})
        else:
            advForm = AdvanceForm()
            return render(res, 'main/advanced.html', {"form": advForm, "title": "Advance Search",'page':'Advance Search' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/advanced.html', {"title": "Advance Search",'page':'Advance Search' ,"to": '/login', "do": "LOGIN"})


## More 
def more(res):
    if res.user.is_authenticated:
        return render(res, 'main/more.html', {"title": "More",'page':'More About' ,"to": '/logout', "do": "LOGOUT"})
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



        