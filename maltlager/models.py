from django.db import models

class Malt(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)

class Hops(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)

class MaltChange(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    time = models.DateTimeField()

class HopsChange(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    time = models.DateTimeField()
