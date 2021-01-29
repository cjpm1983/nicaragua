# Generated by Django 3.1.4 on 2021-01-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostal', '0002_auto_20210113_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Pasaporte', models.CharField(max_length=7)),
                ('Email', models.EmailField(max_length=254)),
                ('HoraEntrada', models.DateTimeField()),
                ('HoraSalida', models.DateTimeField()),
                ('Aerolinea', models.CharField(max_length=200, null=True)),
                ('imagendestacada', models.ImageField(upload_to='imageshostales')),
            ],
        ),
    ]