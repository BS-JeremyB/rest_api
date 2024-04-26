from django.db import models

# Create your models here.
class Realisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nom} {self.prenom}'


class Film(models.Model):
    titre = models.CharField(max_length=200)
    annee_sortie = models.IntegerField()
    realisateur = models.ManyToManyField(Realisateur)
    num_exploitation = models.IntegerField(unique=True)
    affiche = models.ImageField(upload_to='affiches/', null=True, blank=True)

    def __str__(self):
        return self.titre