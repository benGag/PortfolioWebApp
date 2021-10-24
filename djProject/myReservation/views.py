from django.shortcuts import render

def myReservation(request):
    return render(request, "myreservation/home.html")

