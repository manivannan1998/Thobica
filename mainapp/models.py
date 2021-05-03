from django.db import models

# Create your models here.
'''
class Menu(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name
'''
class Register(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    #phone = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    repeat_password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
'''
class Userid(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField()

    class Meta:
        db_table='suscribed_user'

    def __str__(self):
        return self.username 
        ''' 