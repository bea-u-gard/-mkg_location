from django.db import models

class Voiture(models.Model):
    MARQUES = [
    ('BMW', 'BMW'),
    ('Mercedes', 'Mercedes-Benz'),
    ('Audi', 'Audi'),
    ('Range Rover', 'Range Rover'),
    ('Toyota', 'Toyota'),
    ('Peugeot', 'Peugeot'),
    ('Renault', 'Renault'),
    ('Nissan', 'Nissan'),
    ('Kia', 'Kia'),
    ('Hyundai', 'Hyundai'),
    ('Honda', 'Honda'),
    ('Ford', 'Ford'),
    ('Chevrolet', 'Chevrolet'),
    ('Volkswagen', 'Volkswagen'),
    ('Opel', 'Opel'),
    ('Fiat', 'Fiat'),
    ('Citroën', 'Citroën'),
    ('Mazda', 'Mazda'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Volvo', 'Volvo'),
    ('Jaguar', 'Jaguar'),
    ('Land Rover', 'Land Rover'),
    ('Lexus', 'Lexus'),
    ('Subaru', 'Subaru'),
    ('Suzuki', 'Suzuki'),
    ('Dacia', 'Dacia'),
    ('Jeep', 'Jeep'),
    ('Chrysler', 'Chrysler'),
    ('Dodge', 'Dodge'),
    ('Ram', 'Ram'),
    ('Alfa Romeo', 'Alfa Romeo'),
    ('Porsche', 'Porsche'),
    ('Ferrari', 'Ferrari'),
    ('Lamborghini', 'Lamborghini'),
    ('Maserati', 'Maserati'),
    ('Bentley', 'Bentley'),
    ('Rolls-Royce', 'Rolls-Royce'),
    ('Bugatti', 'Bugatti'),
    ('Tesla', 'Tesla'),
    ('Skoda', 'Skoda'),
    ('Seat', 'Seat'),
    ('Mini', 'Mini'),
    ('Aston Martin', 'Aston Martin'),
    ('Infiniti', 'Infiniti'),
    ('Acura', 'Acura'),
    ('Genesis', 'Genesis'),
    ('Saab', 'Saab'),
    ('Hummer', 'Hummer'),
    ('Lincoln', 'Lincoln'),
    ('Cadillac', 'Cadillac'),
    ('GMC', 'GMC'),
    ('Chery', 'Chery'),
    ('Geely', 'Geely'),
    ('BYD', 'BYD'),
    ('Great Wall', 'Great Wall'),
    ('Mahindra', 'Mahindra'),
    ('Tata', 'Tata'),
    ('Proton', 'Proton'),
    ('Perodua', 'Perodua'),
    ('SsangYong', 'SsangYong'),
    ('Isuzu', 'Isuzu'),
    ('Scania', 'Scania'),
    ('MAN', 'MAN'),
]

    marque = models.CharField(max_length=50, choices=MARQUES, verbose_name="Marque")
    modele = models.CharField(max_length=100, verbose_name="Modèle")
    annee = models.IntegerField(verbose_name="Année")
    prix_jour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix par jour (Fcfa)")
    prix_mois = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix par mois (Fcfa)")
    image = models.ImageField(upload_to='voitures/')  # Assure-toi d'avoir upload_to !

    def __str__(self):
        return f"{self.marque} {self.modele} - {self.annee}"



class Reservation(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)  # Référence à la voiture réservée
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Réservation pour {self.voiture} du {self.date_debut} au {self.date_fin}"




class Offre(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='offres/')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
    


class Temoignage(models.Model):
    nom = models.CharField(max_length=100)  # Nom du client
    image = models.ImageField(upload_to='temoignages/')  # Image du client
    avis = models.TextField()  # Témoignage
    etoiles = models.IntegerField(choices=[(1, '1 étoile'), (2, '2 étoiles'), (3, '3 étoiles'), (4, '4 étoiles'), (5, '5 étoiles')])  # Note sur 5 étoiles

    def __str__(self):
        return self.nom


from django.db import models

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)  # L'email de l'abonné
    date_subscribed = models.DateTimeField(auto_now_add=True)  # La date d'abonnement

    def __str__(self):
        return self.email



from django.db import models

class PromotionSlide(models.Model):
    image = models.ImageField(upload_to='promotions/')  # Stocke les images dans le dossier 'promotions/'
    title = models.CharField(max_length=100)  # Titre de la promotion
    description = models.TextField()  # Description de la promotion
    is_active = models.BooleanField(default=True)  # Permet d'activer/désactiver une slide

    def __str__(self):
        return self.title