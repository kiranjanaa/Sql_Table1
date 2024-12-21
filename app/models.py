from django.db import models

# Create your models here.
class Country(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)

class Captial(models.Model):
    ci=models.ForeignKey(Country,on_delete=models.CASCADE)
    cnmae=models.CharField(max_length=100)