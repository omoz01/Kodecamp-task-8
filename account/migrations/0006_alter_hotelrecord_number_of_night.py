# Generated by Django 4.0.5 on 2022-06-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_hotelrecord_number_of_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelrecord',
            name='number_of_night',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]