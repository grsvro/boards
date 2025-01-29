from django.db import models


# Create your models here.
class Task(models.Model):
    date = models.DateField(auto_now_add=True)
    menu = models.CharField(max_length=100)
    age = models.IntegerField()
