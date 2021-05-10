from django.db import models

class Requête(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    image_url=models.CharField(max_length=2000)

class pays(models.Model):
    iso_code=models.CharField(primary_key=True, max_length=3)
    continent=models.CharField(max_length=15,null=True)
    region=models.CharField(max_length=25,null=True)
    country=models.CharField(max_length=35,null=True)
    hdi=models.FloatField(null=True)
    population=models.IntegerField(null=True)
    area_sql_ml=models.IntegerField(null=True)
    climate=models.IntegerField(null=True)
    date_premiere_vaccination=models.DateTimeField(null=True)

    def __str__(self):
        return self.iso_code