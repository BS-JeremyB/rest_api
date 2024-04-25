from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class RealisateurViewSet(viewsets.ModelViewSet):

    queryset = Realisateur.objects.all()
    serializer_class = RealisateurSerializer

    # def get_permissions(self):
    #     if self.action == 'destroy':
    #         return [IsAuthenticated()]
    #     return [AllowAny()]

  

class FilmViewSet(viewsets.ModelViewSet):
    
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    


        
