from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return "%s %s %s" % (self.username, self.email, self.phone)
        # return "%s %s %s" % (self.first_name, self.last_name, self.phone)


# class Address(models.Model):
#     street = models.CharField('street', max_length=1024)
#     city = models.CharField('city', max_length=100)
#     state = models.CharField('state', max_length=3)
#     zip = models.CharField('zip', max_length=6)
#     #referencing 
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)

#     def __str__(self):
#         return "%s %s %s %s" % (self.street, self.city, self.state, self.zip)

#     class Meta:
#         ordering = ['zip']


