# Generated by Django 4.0.6 on 2022-08-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0005_userperfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='userperfil',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]