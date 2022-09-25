from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req, id):
    print (id)
    return HttpResponse("<h1>%s</h1>" % id)


def test(req):
    return HttpResponse("Hello")