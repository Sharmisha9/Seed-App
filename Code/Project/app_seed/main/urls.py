from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('<int:id>', views.index, name="index")
    
]