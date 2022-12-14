# Generated by Django 4.0.4 on 2022-07-05 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_alter_producto_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kardex_categoria', models.CharField(choices=[('calidad', 'calidad'), ('casntidad', 'cantidad')], max_length=100)),
                ('kardex_value', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='productos.producto')),
            ],
        ),
    ]
