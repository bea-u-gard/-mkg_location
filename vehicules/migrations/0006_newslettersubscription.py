# Generated by Django 5.1.7 on 2025-03-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicules', '0005_temoignage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
