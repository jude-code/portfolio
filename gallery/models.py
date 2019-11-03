from django.db import models

# Create your models here.

# modeles 要在admin里注册
class Gallery(models.Model):
    description=models.CharField(max_length=100)
