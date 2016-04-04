from django.db import models

class malt(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)

class hops(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)

class maltchange(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    time = models.DateTimeField()
    user = models.CharField(max_length=100,default="unknown")

class hopschange(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    time = models.DateTimeField()
    user = models.CharField(max_length=100,default="unknown")

class board_member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/board_member')

class activity(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(help_text='Format: YYYY-MM-DD HH:MM')
    content = models.TextField()
