from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxLengthValidator
import datetime
import random
import string

def generate_random_string(length):
        letters_and_digits = string.ascii_uppercase + string.digits
        return ''.join(random.choices(letters_and_digits, k=length))


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
    
class StaffUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    id_number = models.CharField(max_length=10, default='A123456789')
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Female')
    
    birth_date = models.DateField(default='1993-12-20')
    
    USER_TYPE_CHOICES = (
        ('Crew - TA', 'Crew - TA'),
        ('Crew - CA', 'Crew - CA'),
        ('Crew - AP', 'Crew - AP'),
        ('Crew - DP', 'Crew - DP'),
        ('Crew - CP', 'Crew - CP'),
        ('Crew - IC', 'Crew - IC'),
        ('Pilot', 'Pilot'),
        ('Office - DC', 'Office - DC'),
        ('Office - FlightM', 'Office - FlightM'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Crew - TA')
    
    CLASS_CHOISE = (
        ('2023A', '2023A'),
        ('2023B', '2023B'),
        ('2023C', '2023C'),
        ('2023D', '2023D'),
        ('2023E', '2023E'),
    )
    angel_class = models.CharField(max_length=20, choices=CLASS_CHOISE, default='2023A')
    
    times = models.IntegerField(default=0)
    
    employee_id = models.CharField(max_length=8, default=generate_random_string(8))
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = generate_random_string(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username