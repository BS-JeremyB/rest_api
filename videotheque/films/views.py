from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class RealisateurList(generics.ListCreateAPIView):

    queryset = Realisateur.objects.all()
    serializer_class = RealisateurSerializer

    
class RealisateurDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Realisateur.objects.all()
    serializer_class = RealisateurSerializer
 


class FilmList(generics.ListCreateAPIView):
    
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
class FilmDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    

        
