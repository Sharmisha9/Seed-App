from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .form import MyForm


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




## if user is authenticated, then allow to visit, if not, redirect to login

def basic(res):
    return HttpResponse("BASIC")


def advanced(res):
    return HttpResponse("ADVANCED")


def more(res):
    return HttpResponse("MORE")















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



        