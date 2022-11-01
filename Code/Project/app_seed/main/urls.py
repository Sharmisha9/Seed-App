from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('basic/', views.basic, name="basic"),
    path('advanced/', views.advanced, name="advanced"),
    path('more/', views.more, name="more"),
    # path('login/', views.myCreate, name='login'),
    # path('', views.test),
]


