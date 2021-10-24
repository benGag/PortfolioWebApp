from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Reservation(models.Model):
    arrival = models.DateField
    departure = models.DateField
    total_guests = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    