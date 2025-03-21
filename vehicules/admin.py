from django.contrib import admin
from .models import Voiture, Reservation

@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'annee', 'prix_jour', 'prix_mois')
    search_fields = ('marque', 'modele')
    list_filter = ('marque', 'annee')



# Personnaliser l'affichage des réservations dans l'admin
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('voiture', 'nom', 'email', 'telephone', 'date_debut', 'date_fin')
    search_fields = ('nom', 'email', 'voiture__marque')  # Permet la recherche par nom, email ou marque de voiture
    list_filter = ('date_debut', 'date_fin', 'voiture')  # Filtre par dates et voiture

admin.site.register(Reservation, ReservationAdmin)


from django.contrib import admin
from .models import Offre

class OffreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'date_creation', 'image')  # Champs à afficher dans la liste
    search_fields = ('titre', 'description')  # Champs sur lesquels rechercher
    list_filter = ('date_creation',)  # Permet de filtrer les offres par date de création
    ordering = ('-date_creation',)  # Tri par date de création (du plus récent au plus ancien)

admin.site.register(Offre, OffreAdmin)


# admin.py
from django.contrib import admin
from .models import Temoignage

class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'etoiles', 'avis', 'image')  # Colonnes affichées dans la liste des témoignages
    search_fields = ('nom', 'avis')  # Champs sur lesquels effectuer une recherche
    list_filter = ('etoiles',)  # Filtre par nombre d'étoiles

admin.site.register(Temoignage, TemoignageAdmin)


from django.contrib import admin
from .models import NewsletterSubscription

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')  # Colonnes à afficher dans l'admin
    search_fields = ('email',)  # Permet de rechercher un abonnement par email
    list_filter = ('date_subscribed',)  # Filtrer par date d'abonnement

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)



from django.contrib import admin
from .models import PromotionSlide

@admin.register(PromotionSlide)
class PromotionSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')  # Affiche ces champs dans la liste des slides
    list_editable = ('is_active',)  # Permet de modifier 'is_active' directement depuis la liste
    search_fields = ('title', 'description')  # Permet de rechercher par titre ou description

