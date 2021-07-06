# Generated by Django 3.2.5 on 2021-07-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('ocupado', models.BooleanField(default=False)),
                ('detalle', models.CharField(max_length=400)),
                ('precio', models.FloatField()),
                ('dormitorios', models.IntegerField()),
                ('capacidad', models.IntegerField()),
            ],
        ),
    ]
