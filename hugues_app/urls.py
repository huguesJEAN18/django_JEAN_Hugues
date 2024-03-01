from django.urls import path
from . import views

urlpatterns = [
    # Autres URL patterns...
    path('connexion/', views.connexion, name='connexion'),
    path('dashboard/', views.dashboard, name='dashboard'),  # URL pour la vue du tableau de bord
    path('reserver/<int:vol_id>/', views.reserver_vol, name='reserver_vol'),
    path('toutes_reservations/', views.toutes_reservations, name='toutes_reservations'),
]
