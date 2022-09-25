from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(res):
    if res.user.is_authenticated:
        tot = '/logout'
        dot = 'LOGOUT'
    else:
        tot = '/login'
        dot = 'LOGIN'

    if res.method == 'POST':
        form = RegisterForm(res.POST)
        if form.is_valid():
            form.save()
        return redirect('/' )
    else:
        form = RegisterForm()
    return render(res, 'register/register.html', {'form': form, 'page':'REGISTER', 'title': 'Register','to':'/login', 'do': 'LOGIN'})