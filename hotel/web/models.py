from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hotels(models.Model):

    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="TurismoReal") #poner turismoreal
    owner = models.CharField(max_length=20, default="TurismoReal")
    location = models.CharField(max_length=50, default="Ejemplo: Region de chile") #location = puede ser nombres de comunas o regiones
    state = models.CharField(max_length=50,default="Ejemplo: Capital de la region") #state = podria ser la capital
    country = models.CharField(max_length=50,default="Chile") #poner chile
    def __str__(self):
        return self.name


class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "Disponible"), 
    ("2", "No Disponible"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "Premium"), 
    ("2", "VIP"),
    ("3","Basico"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username
