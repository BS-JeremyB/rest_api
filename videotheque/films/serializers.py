from rest_framework import serializers
from .models import *

class RealisateurSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=100)
    prenom = serializers.CharField(max_length=100)
    nationalite = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Realisateur.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nom = validated_data.get('nom', instance.nom)
        instance.prenom = validated_data.get('prenom', instance.prenom)
        instance.nationalite = validated_data.get('nationalite', instance.nationalite)
        instance.save()
        return instance
    

class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titre = serializers.CharField(max_length=200)
    annee_sortie = serializers.IntegerField()
    realisateur = serializers.PrimaryKeyRelatedField(many=True, queryset=Realisateur.objects.all())
    num_exploitation = serializers.IntegerField()


    def create(self, validated_data):
        realisateur = validated_data.pop('realisateur')
        film = Film.objects.create(**validated_data)
        film.realisateur.set(realisateur)
        return film
    

    def update(self, instance, validated_data):
        instance.titre = validated_data.get('titre', instance.titre)
        instance.annee_sortie = validated_data.get('annee_sortie', instance.annee_sortie)
        instance.num_exploitation = validated_data.get('num_exploitation', instance.num_exploitation)
        instance.save()

        if 'realisateur' in validated_data:
            instance.realisateur.set(validated_data['realisateur'])

        return instance
