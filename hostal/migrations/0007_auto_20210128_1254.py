# Generated by Django 3.1.4 on 2021-01-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostal', '0006_auto_20210128_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='Personas',
            field=models.IntegerField(null=True),
        ),
    ]