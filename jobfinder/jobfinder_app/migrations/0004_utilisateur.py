# Generated by Django 4.2 on 2024-10-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfinder_app', '0003_alter_annonces_contrat_alter_annonces_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('telephone', models.CharField(max_length=300)),
                ('mdp', models.TextField()),
            ],
            options={
                'db_table': 'Utilisateur',
            },
        ),
    ]
