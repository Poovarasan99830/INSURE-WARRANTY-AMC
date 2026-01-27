from django.db import models

# Create your models here.
class Appliances(models.Model):
    product=models.CharField(max_length=150)
    brand=models.CharField(max_length=150)
    purchase_date=models.DateField()
