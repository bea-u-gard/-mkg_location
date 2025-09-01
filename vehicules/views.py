from django.http import HttpResponse
from django.shortcuts import render
from .models import Offre, Reservation, Temoignage, Voiture

# views.py
from django.shortcuts import render
from .models import Voiture, Offre

from django.shortcuts import render, redirect
from .forms import NewsletterForm
from django.contrib import messages
from .models import Voiture, Offre, Temoignage, NewsletterSubscription,  PromotionSlide

# def accueil(request):
#     voitures = Voiture.objects.all()  # Récupère toutes les voitures
#     offres = Offre.objects.all()  # Récupère toutes les offres
#     temoignages = Temoignage.objects.all()[:3]  # Limite à 3 témoignages

#     if request.method == 'POST':
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             # Enregistre l'email dans la base de données
#             form.save()
#             messages.success(request, "Merci de vous être abonné à notre newsletter !")
#         else:
#             messages.error(request, "L'email que vous avez saisi est invalide.")
    
#     return render(request, 'vehicules/index.html', {
#         'voitures': voitures,
#         'offres': offres,
#         'temoignages': temoignages,
#         'form': NewsletterForm()  # Passe le formulaire à la vue
#     })



def accueil(request):
    """
    Vue pour la page d'accueil.
    Récupère les voitures, offres, témoignages et slides promotionnelles.
    Gère également l'inscription à la newsletter.
    """
    # Récupérer les données nécessaires
    voitures = Voiture.objects.all()  # Récupère toutes les voitures
    offres = Offre.objects.all()[:3]  # Récupère toutes les offres
    temoignages = Temoignage.objects.all()[:3]  # Limite à 3 témoignages
    slides = PromotionSlide.objects.filter(is_active=True)  # Récupère les slides actives

    # Gestion du formulaire de newsletter
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Enregistre l'email dans la base de données
            form.save()
            messages.success(request, "Merci de vous être abonné à notre newsletter !")
        else:
            messages.error(request, "L'email que vous avez saisi est invalide.")
    else:
        form = NewsletterForm()  # Initialise un formulaire vide pour les requêtes GET

    # Contexte à passer au template
    context = {
        'voitures': voitures,
        'offres': offres,
        'temoignages': temoignages,
        'slides': slides,  # Ajoute les slides promotionnelles
        'form': form,  # Passe le formulaire à la vue
    }

    # Rendre le template avec le contexte
    return render(request, 'vehicules/index.html', context)


from django.shortcuts import render

def confirmation_reservation(request, nom, email, telephone, vehicule, date_debut, date_fin):
    context = {
        'nom': nom,
        'email': email,
        'telephone': telephone,
        'vehicule': vehicule,
        'date_debut': date_debut,
        'date_fin': date_fin,
    }
    return render(request, 'vehicules/confirmation_reservation.html', context)



from django.shortcuts import redirect

def reservation_form(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.POST['nom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        vehicule_id = request.POST['vehicule']
        date_debut = request.POST['date-debut']
        date_fin = request.POST['date-fin']

        # Récupérer l'objet Voiture associé à la sélection
        voiture = Voiture.objects.get(id=vehicule_id)

        # Créer une nouvelle réservation
        reservation = Reservation(
            voiture=voiture,
            nom=nom,
            email=email,
            telephone=telephone,
            date_debut=date_debut,
            date_fin=date_fin
        )
        reservation.save()

        # Rediriger vers la page de confirmation
        return redirect('confirmation_reservation', nom=nom, email=email, telephone=telephone, vehicule=voiture.marque + " " + voiture.modele, date_debut=date_debut, date_fin=date_fin)

    # Si la méthode est GET, afficher le formulaire avec les voitures disponibles
    voitures = Voiture.objects.all()
    return render(request, 'vehicules/index.html', {'voitures': voitures})
# section dashboard voiture

from django.shortcuts import render

# Créez une fonction pour la page de votre dashboard
# def dashboard(request):
#     return render(request, 'dashboard/dash.html')

from django.shortcuts import render

def dashboard(request):
    if not request.session.get('is_logged_in'):  # Vérifier si l'utilisateur est connecté
        return redirect('login')  # Rediriger vers la page de connexion si non connecté
    return render(request, 'dashboard/dash.html')  # Afficher le tableau de bord


from django.shortcuts import render, get_object_or_404, redirect
from .models import Voiture
from .forms import VoitureForm

def liste_voitures(request):
    voitures = Voiture.objects.all()
    return render(request, 'dashboard/voitures/liste_voitures.html', {'voitures': voitures})

def ajouter_voiture(request):
    if request.method == 'POST':
        form = VoitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_voitures')
    else:
        form = VoitureForm()
    return render(request, 'dashboard/voitures/ajouter_voiture.html', {'form': form})

def modifier_voiture(request, id):
    voiture = get_object_or_404(Voiture, id=id)
    if request.method == 'POST':
        form = VoitureForm(request.POST, request.FILES, instance=voiture)
        if form.is_valid():
            form.save()
            return redirect('liste_voitures')
    else:
        form = VoitureForm(instance=voiture)
    return render(request, 'dashboard/voitures/modifier_voiture.html', {'form': form})

def supprimer_voiture(request, id):
    voiture = get_object_or_404(Voiture, id=id)
    if request.method == 'POST':
        voiture.delete()
        return redirect('liste_voitures')
    return render(request, 'dashboard/voitures/supprimer_voiture.html', {'voiture': voiture})
# fin section dashboard voiture





# section dashboard reservation
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm

def liste_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'dashboard/reservation/liste_reservations.html', {'reservations': reservations})

def ajouter_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'dashboard/reservation/ajouter_reservation.html', {'form': form})

def modifier_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('liste_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'dashboard/reservation/modifier_reservation.html', {'form': form})

def supprimer_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('liste_reservations')
    return render(request, 'dashboard/reservation/supprimer_reservation.html', {'reservation': reservation})
    
# fin section dashboard reservation



# section dashboard offres

from django.shortcuts import render, get_object_or_404, redirect
from .models import Offre
from .forms import OffreForm

def liste_offres(request):
    offres = Offre.objects.all()
    return render(request, 'dashboard/offres/liste_offres.html', {'offres': offres})

def ajouter_offre(request):
    if request.method == 'POST':
        form = OffreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_offres')
    else:
        form = OffreForm()
    return render(request, 'dashboard/offres/ajouter_offre.html', {'form': form})

def modifier_offre(request, id):
    offre = get_object_or_404(Offre, id=id)
    if request.method == 'POST':
        form = OffreForm(request.POST, request.FILES, instance=offre)
        if form.is_valid():
            form.save()
            return redirect('liste_offres')
    else:
        form = OffreForm(instance=offre)
    return render(request, 'dashboard/offres/modifier_offre.html', {'form': form})

def supprimer_offre(request, id):
    offre = get_object_or_404(Offre, id=id)
    if request.method == 'POST':
        offre.delete()
        return redirect('liste_offres')
    return render(request, 'dashboard/offres/supprimer_offre.html', {'offre': offre})
# fin section dashboard offres



#section dashboard temoignages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Temoignage
from .forms import TemoignageForm

def liste_temoignages(request):
    temoignages = Temoignage.objects.all()
    return render(request, 'dashboard/temoignages/liste_temoignages.html', {'temoignages': temoignages})

def ajouter_temoignage(request):
    if request.method == 'POST':
        form = TemoignageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_temoignages')
    else:
        form = TemoignageForm()
    return render(request, 'dashboard/temoignages/ajouter_temoignage.html', {'form': form})

def modifier_temoignage(request, id):
    temoignage = get_object_or_404(Temoignage, id=id)
    if request.method == 'POST':
        form = TemoignageForm(request.POST, request.FILES, instance=temoignage)
        if form.is_valid():
            form.save()
            return redirect('liste_temoignages')
    else:
        form = TemoignageForm(instance=temoignage)
    return render(request, 'dashboard/temoignages/modifier_temoignage.html', {'form': form})

def supprimer_temoignage(request, id):
    temoignage = get_object_or_404(Temoignage, id=id)
    if request.method == 'POST':
        temoignage.delete()
        return redirect('liste_temoignages')
    return render(request, 'dashboard/temoignages/supprimer_temoignage.html', {'temoignage': temoignage})

# fin section dashboard temoignages

#  section dashboard affiche

from django.shortcuts import render, get_object_or_404, redirect
from .models import PromotionSlide
from .forms import PromotionSlideForm
from django.contrib import messages

# Afficher la liste des affiches publicitaires
def liste_affiches(request):
    affiches = PromotionSlide.objects.all()
    return render(request, 'dashboard/affiche/liste_affiches.html', {'affiches': affiches})
# Ajouter une nouvelle affiche publicitaire
def ajouter_affiche(request):
    if request.method == 'POST':
        form = PromotionSlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "L'affiche publicitaire a été ajoutée avec succès.")
            return redirect('liste_affiches')
    else:
        form = PromotionSlideForm()
    return render(request, 'dashboard/affiche/ajouter_affiche.html', {'form': form})

# Modifier une affiche publicitaire existante
def modifier_affiche(request, id):
    affiche = get_object_or_404(PromotionSlide, id=id)
    if request.method == 'POST':
        form = PromotionSlideForm(request.POST, request.FILES, instance=affiche)
        if form.is_valid():
            form.save()
            messages.success(request, "L'affiche publicitaire a été modifiée avec succès.")
            return redirect('liste_affiches')
    else:
        form = PromotionSlideForm(instance=affiche)
    return render(request, 'dashboard/affiche/modifier_affiche.html', {'form': form, 'affiche': affiche})

# Supprimer une affiche publicitaire
def supprimer_affiche(request, id):
    affiche = get_object_or_404(PromotionSlide, id=id)
    if request.method == 'POST':
        affiche.delete()
        messages.success(request, "L'affiche publicitaire a été supprimée avec succès.")
        return redirect('liste_affiches')
    return render(request, 'dashboard/affiche/supprimer_affiche.html', {'affiche': affiche})

# fin section dashboard affiche





# section dashboard Abonnes
from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsletterSubscription
from .forms import NewsletterSubscriptionForm

def liste_abonnes(request):
    abonnes = NewsletterSubscription.objects.all()
    return render(request, 'dashboard/abonnes/liste_abonnes.html', {'abonnes': abonnes})

def supprimer_abonne(request, id):
    abonne = get_object_or_404(NewsletterSubscription, id=id)
    if request.method == 'POST':
        abonne.delete()
        return redirect('liste_abonnes')
    return render(request, 'dashboard/abonnes/supprimer_abonne.html', {'abonne': abonne})
# fin section dashboard Abonnes

# section dashboard Connexion admin
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')  # Récupérer le nom d'utilisateur
        password = request.POST.get('password')  # Récupérer le mot de passe

        # Vérifier si username et password sont "location"
        if username == 'Guillaume' and password == 'locationMKG2000':
            request.session['is_logged_in'] = True  # Stocker l'état de connexion dans la session
            return redirect('dashboard')  # Rediriger vers le tableau de bord
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'dashboard/authentification/login.html')  # Page de connexion

from django.shortcuts import render

def custom_logout(request):
    request.session.pop('is_logged_in', None)  # Supprimer l'état de connexion de la session
    return render(request, 'dashboard/authentification/logout.html')  # Afficher la page de déconnexion


