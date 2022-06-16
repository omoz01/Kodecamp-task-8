# Generated by Django 4.0.5 on 2022-06-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_hotelrecord_number_of_night_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelrecord',
            name='number_of_night',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='hotelrecord',
            name='occupant_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotelrecord',
            name='occupant_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='hotelrecord',
            name='occupant_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotelrecord',
            name='occupant_occupation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotelrecord',
            name='room_number',
            field=models.IntegerField(default=1),
        ),
    ]
