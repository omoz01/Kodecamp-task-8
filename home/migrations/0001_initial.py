# Generated by Django 4.0.5 on 2022-06-16 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OccupantDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupant_name', models.CharField(max_length=200)),
                ('occupant_address', models.CharField(max_length=200)),
                ('occupant_email', models.EmailField(max_length=254)),
                ('occupant_age', models.IntegerField()),
                ('occupant_occupation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_night', models.IntegerField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('occupant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.occupantdetails')),
            ],
        ),
    ]
