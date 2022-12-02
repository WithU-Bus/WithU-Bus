from django.db import models

class Bus(models.Model):
    BUS = models.IntegerField()
    NUMBER = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=20)
    UNIQUEID = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    WAY = models.CharField(max_length=10)

    class Meta:
        db_table = 'bus'
        app_label = 'app'
        ordering = ['BUS', 'NUMBER', 'NAME', 'UNIQUEID', 'lat', 'lng', 'WAY']
        managed = False
    
    def __str__(self):
        return(self.BUS, self.NUMBER, self.NAME, self.UNIQUEID, self.lat, self.lng, self.WAY)


class Infra(models.Model):
    NUMBER = models.AutoField(primary_key=True)
    TYPE = models.CharField(max_length=20)
    ADDRESS = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    Tel = models.CharField(max_length=20)
    NAME = models.CharField(max_length=20)
    URL = models.CharField(max_length=20)

    class Meta:
        db_table = 'infra'
        app_label = 'app'
        ordering = ['NUMBER', 'TYPE', 'ADDRESS', 'lat', 'lng', 'Tel', 'NAME', 'URL']
        managed = False
    
    def __str__(self):
        return(self.NUMBER, self.TYPE, self.ADDRESS, self.lat, self.lng, self.Tel, self.NAME, self.URL)
