from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)