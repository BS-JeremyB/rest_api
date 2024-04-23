from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
@csrf_exempt
def realisateur_list(request):

    if request.method == 'GET':
        realisateurs = Realisateur.objects.all()
        serializer = RealisateurSerializer(realisateurs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RealisateurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def realisateur_detail(request, id):
    try:
        realisateur = Realisateur.objects.get(id=id)
    except Realisateur.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = RealisateurSerializer(realisateur)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RealisateurSerializer(instance=realisateur, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        realisateur.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)