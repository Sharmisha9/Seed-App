from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .form import MyForm


# Create your views here.
def index(res):
    if res.user.is_authenticated:
        return render(res, 'main/index.html', {"title": "Home",'page':'CS440 HOME' ,"to": '/logout', "do": "LOGOUT"})
    else:
        return render(res, 'main/index.html', {"title": "Home", 'page':'CS440 HOME' ,"to": "/login", "do": "LOGIN"})


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



        