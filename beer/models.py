from django.db import models

class Reading(models.Model):
    date        = models.DateTimeField('date of reading')
    temperature = models.IntegerField()
    gravity     = models.FloatField() 

class Batch(models.Model):
    date        = models.DateTimeField('date created')
    title       = models.CharField(max_length=200)
    readings    = models.ForeignKey(Reading)

