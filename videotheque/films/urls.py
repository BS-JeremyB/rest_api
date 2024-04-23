from django.urls import path
from . import views

urlpatterns = [
    path('realisateur/', views.realisateur_list, name='liste_realisateur'),
    path('realisateur/<int:id>', views.realisateur_detail, name='detail_realisateur'),
    path('film/', views.film_list, name='liste_realisateur'),
    path('film/<int:id>', views.film_detail, name='detail_realisateur')
]
