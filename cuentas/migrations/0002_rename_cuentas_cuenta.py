# Generated by Django 4.0.4 on 2022-06-21 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuentas',
            new_name='Cuenta',
        ),
    ]
