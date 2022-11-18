from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Soil(models.Model):
    soil_type = models.CharField(max_length=100)

    def _str_(self):
        return "%s" % (self.type)

class Season(models.Model):
    season = models.CharField(max_length=100)
    def _str_(self):
        return "%s" % (self.season)


class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE)
    def _str_(self):
        return "%s %s %s" % (self.name, self.season, self.soil)

# advanced Form
class CropAdv(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE)
    
    max_temp = models.FloatField()
    min_temp = models.FloatField()

    max_humidity = models.FloatField()
    min_humidity = models.FloatField()

    max_pH = models.FloatField()
    min_pH = models.FloatField()
    def __str__(self):
        return "%s %s %s %f %f %f %f %f %f" % (self.name, self.season, self.soil, self.max_temp, self.min_temp, self.max_humidity, self.min_humidity, self.max_pH, self.min_pH)

## Advanced Image Form
class CropDesc(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def _str_(self):
        return "%s %s" % (self.name, self.desc)

class ImageFormModel(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to = "images/")    

    def _str_(self):
        return self.name







