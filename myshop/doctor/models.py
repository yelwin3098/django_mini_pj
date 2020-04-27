from django.db import models

class Category(models.Model):
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=225)
    name=models.CharField(max_length=225)

class Doctor(models.Model):
    name=models.CharField(max_length=150)
    quali=models.TextField()
    duty=models.TextField()
    category=models.IntegerField()
