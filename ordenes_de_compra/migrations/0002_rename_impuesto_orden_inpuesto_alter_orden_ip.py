# Generated by Django 4.0.6 on 2022-07-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_de_compra', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='impuesto',
            new_name='inpuesto',
        ),
        migrations.AlterField(
            model_name='orden',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
