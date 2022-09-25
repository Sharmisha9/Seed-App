from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Address(models.Model):
    street = models.CharField('street', max_length=1024)
    city = models.CharField('city', max_length=100)
    state = models.CharField('state', max_length=3)
    zip = models.CharField('zip', max_length=6)
    #referencing 
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.zip

    class Meta:
        ordering = ['zip']
