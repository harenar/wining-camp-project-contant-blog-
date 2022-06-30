from django.db import models
class Service(models.Model):
    username  = models.CharField(max_length=50)
    Ctitle = models.CharField(max_length=50)
    description = models.TextField()


#Create your models here.

class Reg(models.Model):
    name = models.CharField(max_length=50 )
    reg_user_name = models.CharField(max_length=50 )
    password = models.CharField(max_length=50 )
