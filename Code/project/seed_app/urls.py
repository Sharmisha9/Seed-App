from django.urls import path
from . import views



app_name = 'seed_app'

urlpatterns = [
    path('', views.home, name="homepage")
]
