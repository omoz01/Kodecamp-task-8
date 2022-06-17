from django.shortcuts import render, redirect
from .models import HotelRecord

# Create your views here.
def booking(request):
    if request.method == "POST":
        name = request.POST.get("occupant_name")
        address = request.POST.get("occupant_address")
        email = request.POST.get("occupant_email")
        occupation = request.POST.get("occupant_occupation")
        number_of_night = request.POST.get("number_of_night")
        room_number = request.POST.get("room_number")
        amount_paid = request.POST.get("amount_paid")
        s_date = request.POST.get("start_date")
        e_date = request.POST.get("end_date")

        new_record = HotelRecord(occupant_name=name, occupant_address=address, occupant_email=email, occupant_occupation=occupation, number_of_night=number_of_night, room_number=room_number, amount_paid=amount_paid, start_date=s_date, end_date=e_date)
        print("succesful")
        new_record.save()
        return redirect("home:index")
    return render(request, "account/booking.html",)