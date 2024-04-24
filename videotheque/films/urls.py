from django.urls import path
from . import views

urlpatterns = [
    path('realisateur/', views.RealisateurList.as_view(), name='liste_realisateur'),
    path('realisateur/<int:id>', views.RealisateurDetail.as_view(), name='detail_realisateur'),
    path('film/', views.FilmList.as_view(), name='liste_film'),
    path('film/<int:id>', views.FilmDetail.as_view(), name='detail_film')
]
