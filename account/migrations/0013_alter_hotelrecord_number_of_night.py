# Generated by Django 4.0.5 on 2022-06-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_hotelrecord_number_of_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelrecord',
            name='number_of_night',
            field=models.IntegerField(),
        ),
    ]
