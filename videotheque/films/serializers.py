from rest_framework import serializers
from .models import *

class RealisateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realisateur
        fields = '__all__'

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    realisateur_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Realisateur.objects.all(),
        write_only=True,
        source='realisateur'
    )
    realisateur = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='realisateur-detail'
    )

    class Meta:
        model = Film
        fields = ['url','id', 'titre', 'annee_sortie', 'realisateur', 'realisateur_id', 'num_exploitation','affiche']

