from rest_framework import serializers
from .models import *

class RealisateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realisateur
        fields = ['url', 'id', 'nom','prenom','nationalite','film_set']

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

