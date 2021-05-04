# Generated by Django 3.1.4 on 2021-05-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostal', '0014_auto_20210504_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizado'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creada'),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizada'),
        ),
    ]
