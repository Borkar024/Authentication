from django.db import models

class Employee(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)