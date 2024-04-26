from django.db import models
import os
from django.utils.text import slugify

#Custom MKDIR

def film_directory_path(instance, filename):
    # Obtient un titre de film nettoyé et crée un chemin pour l'affiche
    # Utilise 'slugify' pour assurer la compatibilité du chemin de fichier
    base_filename, file_extension = os.path.splitext(filename)
    clean_title = slugify(instance.titre)
    return f'affiches/{clean_title}/{base_filename}{file_extension}'




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
    affiche = models.ImageField(upload_to=film_directory_path, null=True, blank=True)

    def __str__(self):
        return self.titre