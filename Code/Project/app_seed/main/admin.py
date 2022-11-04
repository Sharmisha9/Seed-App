# Register your models here. (showing admin db.)
from django.contrib import admin
from .models import Crop, Soil,Season

admin.site.register(Crop)
admin.site.register(Soil)
admin.site.register(Season)



