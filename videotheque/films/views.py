from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import *
from .serializers import *

# Create your views here.
class RealisateurViewSet(viewsets.ModelViewSet):

    queryset = Realisateur.objects.all()
    serializer_class = RealisateurSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['nom', 'nationalite']
    ordering_fields = ['id', 'nom']
    ordering = ['-id']

    # def get_permissions(self):
    #     if self.action == 'destroy':
    #         return [IsAuthenticated()]
    #     return [AllowAny()]

  

class FilmViewSet(viewsets.ModelViewSet):
    
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    


        
