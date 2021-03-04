from django.db import models

class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=30)
    grades = models.IntegerField()