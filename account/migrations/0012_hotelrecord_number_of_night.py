# Generated by Django 4.0.5 on 2022-06-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_hotelrecord_number_of_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelrecord',
            name='number_of_night',
            field=models.IntegerField(default=1),
        ),
    ]
