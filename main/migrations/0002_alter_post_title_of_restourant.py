# Generated by Django 4.1.5 on 2023-01-24 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_of_restourant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='restourant_name', to='main.restaurant'),
        ),
    ]
