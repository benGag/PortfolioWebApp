from django.shortcuts import render
from django.http import HttpResponse
import random


def myApp(request):
  random_number = random.randint(0, 1000)

  context = {
    "name": "Junior", 
    "random_number": random_number
  }

  return render(request, "myApp/home.html", context)

