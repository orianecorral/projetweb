# Generated by Django 3.0.7 on 2024-10-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfinder_app', '0002_auto_20241011_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonces',
            name='contrat',
            field=models.CharField(choices=[('CDI', 'CDI'), ('CDD 6 mois', 'CDD 6 mois'), ('CDD 12 mois', 'CDD 12 mois'), ('CDD 18 mois', 'CDD 18 mois'), ('Stage', 'Stage'), ('Stage 6 mois', 'Stage 6 mois'), ('Alternance', 'Alternance')], max_length=300),
        ),
    ]
