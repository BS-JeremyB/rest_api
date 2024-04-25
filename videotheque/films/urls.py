from django.urls import path
from . import views

urlpatterns = [
    path('realisateur/', views.RealisateurList.as_view(), name='realisateur-list'),
    path('realisateur/<int:pk>/', views.RealisateurDetail.as_view(), name='realisateur-detail'),
    path('film/', views.FilmList.as_view(), name='film-list'),
    path('film/<int:pk>/', views.FilmDetail.as_view(), name='film-detail'),
]