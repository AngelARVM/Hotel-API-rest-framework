# Generated by Django 3.2.5 on 2021-07-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_auto_20210706_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.IntegerField(max_length=14),
        ),
    ]