from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class User(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Location(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Room(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
class Board(models.Model):
    mac_address_board = models.CharField(max_length=255, primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    remark = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Data(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    power_ct = models.CharField(max_length=255)
    water = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Report(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    power_ct = models.CharField(max_length=255)
    water = models.CharField(max_length=255)
    power_ct_cost = models.CharField(max_length=255)
    water_cost = models.CharField(max_length=255)
    Total_cost = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


