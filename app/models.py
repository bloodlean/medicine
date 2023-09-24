from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=256)
    phone_number = models.TextField()

class Blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField()

class Sponsor(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField()