# Generated by Django 5.1.7 on 2025-03-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='image',
            field=models.ImageField(upload_to='voitures/'),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='prix_jour',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix par jour (Fcfa)'),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='prix_mois',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix par mois (Fcfa)'),
        ),
    ]
