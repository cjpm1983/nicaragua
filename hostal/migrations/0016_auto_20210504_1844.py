# Generated by Django 3.1.4 on 2021-05-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostal', '0015_auto_20210504_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Pasaporte',
            field=models.CharField(max_length=20),
        ),
    ]
