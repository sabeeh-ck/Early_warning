from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    type = models.CharField(max_length=12)

class User(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE ,default="")
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    # age = models.CharField(max_length=4)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=6)
    photo = models.CharField(max_length=100)

class Complaint(models.Model):
    complaint = models.CharField(max_length=50,default="")
    date = models.DateField()
    reply = models.CharField(max_length=50,default="pending")
    status = models.CharField(max_length=50,default="pending")
    USER = models.ForeignKey(User,on_delete=models.CASCADE, default="")

class Division(models.Model):
    division = models.CharField(max_length=100)

class Station(models.Model):
    DIVISION = models.ForeignKey(Division,on_delete=models.CASCADE ,default="")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=7)

class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500, default="")
    CATEGORY = models.ForeignKey(Category,on_delete=models.CASCADE ,default="")

class Forest_officer(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE ,default="")
    STATION = models.ForeignKey(Station,on_delete=models.CASCADE ,default="")
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=34)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=6)
    photo = models.CharField(max_length=100)

class Allocation(models.Model):
    STATION = models.ForeignKey(Station,on_delete=models.CASCADE ,default="")
    OFFICER = models.ForeignKey(Forest_officer,on_delete=models.CASCADE ,default="")
    date = models.DateField()
    status = models.CharField(max_length=22)

class Reservrd_animal(models.Model):
    ANIMAL = models.ForeignKey(Animal,on_delete=models.CASCADE ,default="")

class Notification(models.Model):
    content = models.CharField(max_length=100)
    date = models.DateField()
    OFFICER = models.ForeignKey(Forest_officer,on_delete=models.CASCADE ,default="")

class Alert(models.Model):
    OFFICER = models.ForeignKey(Forest_officer,on_delete=models.CASCADE ,default="")
    date = models.DateField()
    alert = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

class Animal_notification(models.Model):
    detected = models.CharField(max_length=100, default="")
    content = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=100)
    