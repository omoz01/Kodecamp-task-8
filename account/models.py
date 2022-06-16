from django.db import models

# Create your models here.
class HotelRecord(models.Model):
    occupant_name= models.CharField(max_length=200)
    occupant_address= models.CharField(max_length=200)
    occupant_email= models.EmailField()
    occupant_occupation= models.CharField(max_length=200)
    number_of_night= models.IntegerField() 
    room_number= models.IntegerField()
    amount_paid= models.DecimalField(max_digits=10, decimal_places=2)
    start_date= models.DateField()
    end_date= models.DateField()

    def __str__(self):
        return self.occupant_name


