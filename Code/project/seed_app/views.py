
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def loginMethod(req):
    return render(req, 'login.html', {'date': 'Kim'})
    # return HttpResponse("Kim")

def registerMethod(req):
    return render(req, 'register.html', {})