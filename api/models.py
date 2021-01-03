from django.db import models

# Create your models here.

class Sensor(models.Model):
    c_time = models.IntegerField()
    tem = models.IntegerField()
    hum = models.IntegerField()
    water = models.IntegerField()
    light = models.IntegerField()

    def __str__(self):
        return self.c_time
