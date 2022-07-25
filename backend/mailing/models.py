from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _


class EmailTemplate(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    alias = models.CharField(max_length=50)