from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil de l'application véhicules
    path('reservation/', views.reservation_form, name='reservation_form'),  # URL pour le formulaire de réservation


# section dashboard voiture
    path('dashboard/', views.dashboard, name='dashboard'),
    path('voitures/', views.liste_voitures, name='liste_voitures'),
    path('voitures/ajouter/', views.ajouter_voiture, name='ajouter_voiture'),
    path('voitures/modifier/<int:id>/', views.modifier_voiture, name='modifier_voiture'),
    path('voitures/supprimer/<int:id>/', views.supprimer_voiture, name='supprimer_voiture'),


# section dashboard reservation

    path('reservations/', views.liste_reservations, name='liste_reservations'),
    path('reservations/ajouter/', views.ajouter_reservation, name='ajouter_reservation'),
    path('reservations/modifier/<int:id>/', views.modifier_reservation, name='modifier_reservation'),
    path('reservations/supprimer/<int:id>/', views.supprimer_reservation, name='supprimer_reservation'),
    path('confirmation/<str:nom>/<str:email>/<str:telephone>/<str:vehicule>/<str:date_debut>/<str:date_fin>/', views.confirmation_reservation, name='confirmation_reservation'),


# section dashboard offres
    path('offres/', views.liste_offres, name='liste_offres'),
    path('offres/ajouter/', views.ajouter_offre, name='ajouter_offre'),
    path('offres/modifier/<int:id>/', views.modifier_offre, name='modifier_offre'),
    path('offres/supprimer/<int:id>/', views.supprimer_offre, name='supprimer_offre'),


# section dashboard temoignages
    path('temoignages/', views.liste_temoignages, name='liste_temoignages'),
    path('temoignages/ajouter/', views.ajouter_temoignage, name='ajouter_temoignage'),
    path('temoignages/modifier/<int:id>/', views.modifier_temoignage, name='modifier_temoignage'),
    path('temoignages/supprimer/<int:id>/', views.supprimer_temoignage, name='supprimer_temoignage'),
    
    
# section dashboard Abonnes   
    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),
    #path('abonnes/ajouter/', views.ajouter_abonne, name='ajouter_abonne'),
    #path('abonnes/modifier/<int:id>/', views.modifier_abonne, name='modifier_abonne'),
    path('abonnes/supprimer/<int:id>/', views.supprimer_abonne, name='supprimer_abonne'),


# section dashboard Admin
    path('login/', views.custom_login, name='login'),  # URL pour la page de connexion
    path('logout/', views.custom_logout, name='logout'),  # URL pour la déconnexion
    path('dashboard/', views.dashboard, name='dashboard'),  # URL pour le tableau de bord

# Section Dashboard Affiche
    path('affiche/', views.liste_affiches, name='liste_affiches'),
    path('affiche/ajouter/', views.ajouter_affiche, name='ajouter_affiche'),
    path('affiche/modifier/<int:id>/', views.modifier_affiche, name='modifier_affiche'),
    path('affiche/supprimer/<int:id>/', views.supprimer_affiche, name='supprimer_affiche'),
]
