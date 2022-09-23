from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginMethod),
    path('register/', views.registerMethod)
]