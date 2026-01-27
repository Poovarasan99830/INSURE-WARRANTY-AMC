from django.db import models

# Create your models here.


class Appliance(models.Model):
    Product=models.CharField()
    Brand=models.CharField()
    Purchase_Date=models.DateField()

