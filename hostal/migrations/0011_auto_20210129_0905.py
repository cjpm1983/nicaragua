# Generated by Django 3.1.4 on 2021-01-29 09:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('hostal', '0010_auto_20210129_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='Imagen_Pasaje',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='reservaciones/pasaje'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='Imagen_Pasaporte',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='reservaciones/pasaportes'),
        ),
    ]
