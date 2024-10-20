# Generated by Django 3.0.7 on 2024-10-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfinder_compte', '0003_alter_entreprises_id_alter_particuliers_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprises',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='particuliers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]