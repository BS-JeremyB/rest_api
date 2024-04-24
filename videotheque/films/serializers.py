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
    realisateurs = RealisateurSerializer(
        many=True,
        read_only =True,
        source='realisateur'
    )

    class Meta:
        model = Film
        fields = ['id','titre','annee_sortie','realisateurs', 'realisateur_id','num_exploitation']

