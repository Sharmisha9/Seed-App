from django.shortcuts import render, redirect
from .forms import RegisterForm, File
from django.http import HttpResponse


# Create your views here.
def register(res):
    if res.method == 'POST':
        form = RegisterForm(res.POST)
        if form.is_valid():
            form.save()
        return redirect('/' )
    else:
        form = RegisterForm(res.POST)
    return render(res, 'register/register.html', {'form': form, 'page':'REGISTER', 'title': 'Register','to':'/login', 'do': 'LOGIN'})


def upload(res):
    if res.user.is_superuser:
        if res.method == 'POST':
            form = File(res.POST, res.FILES)
            print("BEFORE VALIDATION: ", res)

            if form.is_valid(): 
                print("Handle file HERE using a Funtion")




                return redirect('/')
            return redirect('/')
            # return render(res, 'fileUpload/fileupload.html', {'form':form, 'page':'UPLOAD', 'title': 'File upload','to':'/logout', 'do': 'LOGOUT'})
        else:
            form = File()
            return render(res, 'fileUpload/fileupload.html', {'form':form, 'page':'UPLOAD', 'title': 'File upload','to':'/logout', 'do': 'LOGOUT'})
    else:
        return render(res, 'error/access_limit.html', {'page':'Access Error', 'title': 'Access Error','to':'/login', 'do': 'LOGIN'})
