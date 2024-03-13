from django.db import models

# Create your models here.


class Cars(models.Model):
    name=models.CharField(max_length=1000)
    year=models.CharField(max_length=5)
    price=models.CharField(max_length=100)
    type=models.CharField(max_length=1000)
    id = models.AutoField(primary_key=True)
    photo=models.CharField(max_length=1000000)  # se espera una url de la foto
    description=models.CharField(max_length=10000000)
    title_description=models.CharField(max_length=100000)

class Car_Features(models.Model):
    id_car=models.CharField(max_length=100000)
    title=models.CharField(max_length=10000)
    description=models.CharField(max_length=10000)
    photo=models.CharField(max_length=1000000)  # se espera una url de la foto

class Car_Info(models.Model):
    id_car=models.CharField(max_length=100000)
    photo=models.CharField(max_length=1000000)  # se espera una url de la foto
    title=models.CharField(max_length=100000)
    description=models.CharField(max_length=10000)



    