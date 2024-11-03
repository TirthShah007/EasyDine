from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#book table model
class Booking(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    people = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name







    

#inbuilt user for authentication

class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username



    




    










    

