# Generated by Django 4.0.5 on 2022-06-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OccupantDetails',
            new_name='OccupantDetail',
        ),
        migrations.AlterField(
            model_name='hotelrecord',
            name='number_of_night',
            field=models.IntegerField(),
        ),
    ]
