from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=60)
    age=models.CharField(max_length=2)
