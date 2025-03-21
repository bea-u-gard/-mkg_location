from django import forms
from .models import NewsletterSubscription

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Entrez votre email', 'class': 'form-control'}),
        }


from django import forms
from .models import Voiture

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'annee', 'prix_jour', 'prix_mois', 'image']
        
        
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['voiture', 'nom', 'email', 'telephone', 'date_debut', 'date_fin']
        
from django import forms
from .models import Offre

class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ['titre', 'description', 'image']
        
from django import forms
from .models import Temoignage

class TemoignageForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = ['nom', 'image', 'avis', 'etoiles']
        
from django import forms
from .models import NewsletterSubscription

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        
        
from django import forms
from .models import PromotionSlide

class PromotionSlideForm(forms.ModelForm):
    class Meta:
        model = PromotionSlide
        fields = ['image', 'title', 'description', 'is_active']