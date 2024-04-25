from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

# Create your views here.
class RealisateurList(APIView):
    

    def get(self, request, format=None):
        realisateurs = Realisateur.objects.all()
        serializer = RealisateurSerializer(realisateurs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RealisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class RealisateurDetail(APIView):
    

    def get_object(self,pk):
        try:
            return Realisateur.objects.get(pk=pk)
        except Realisateur.DoesNotExist:
            raise NotFound(detail="Ce réalisateur n'existe pas")
    

    def get(self, request, pk):
        realisateur = self.get_object(pk)
        serializer = RealisateurSerializer(realisateur)
        return Response(serializer.data)
    
    def put(self, request, pk):
        realisateur = self.get_object(pk)
        serializer = RealisateurSerializer(instance=realisateur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        realisateur = self.get_object(pk)
        realisateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class FilmList(APIView):
    

    def get(self, request, format=None):
        # if not request.user.is_authenticated:
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FilmSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class FilmDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise NotFound(detail="Le film avec l'ID spécifié est introuvable.")

    def get(self, request, pk):
        film = self.get_object(pk)
        serializer = FilmSerializer(film, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        film = self.get_object(pk)
        serializer = FilmSerializer(film, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        film = self.get_object(pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
