from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    id_number = models.CharField(max_length=10, default='A123456789')
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Female')
    
    birth_date = models.DateField(default='1993-12-20')
    
    USER_TYPE_CHOICES = (
        ('Pessanger', 'Pessanger'),
        ('Crew', 'Crew'),
        ('Pilot', 'Pilot'),
        ('Office', 'Office'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Pessanger')
    
    miles = models.IntegerField(default=0)
    
    LEVEL_CHOICES = (
        ('Green', 'Green'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Diamond', 'Diamond'),
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Green')

    def __str__(self):
        return self.user.username