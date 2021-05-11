from django.db import models
import uuid

class Requête(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    image_url=models.CharField(max_length=2000)

"""class personne(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length= 20,null=True)
    prenom = models.CharField(max_length= 20,null=True)
    pseudo = models.CharField(max_length= 20,null=True)
    mdp = models.CharField(max_length=20,null=True)
    adresse = models.CharField(max_length=100,null=True)"""
"""class epidemiologiste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    centre = models.CharField(max_length= 20,null=True)
    tel_service = models.IntegerField(null=True)"""