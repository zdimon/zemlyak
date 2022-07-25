from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(default='', max_length=250)
    gender = models.CharField(default='m', max_length=1)

class Prof(models.Model):
    name = models.CharField(default='', max_length=250)
    