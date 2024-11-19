from django.db import models

# Create your models here.
class Progamer(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)