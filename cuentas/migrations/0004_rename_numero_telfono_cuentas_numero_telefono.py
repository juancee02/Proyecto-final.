# Generated by Django 4.0.4 on 2022-06-22 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_rename_cuenta_cuentas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuentas',
            old_name='numero_telfono',
            new_name='numero_telefono',
        ),
    ]