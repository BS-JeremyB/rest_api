from rest_framework import serializers
from .models import Realisateur, Film

class RealisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisateur
        fields = '__all__'

from rest_framework import serializers
from .models import *

class RealisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisateur
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    realisateur_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Realisateur.objects.all(),
        write_only=True,
        source='realisateur'
    )
    realisateur = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detail_realisateur'
    )

    class Meta:
        model = Film
        fields = ['id', 'titre', 'annee_sortie', 'realisateur', 'realisateur_id', 'num_exploitation']

