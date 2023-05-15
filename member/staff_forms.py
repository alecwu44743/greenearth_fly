from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
import uuid
from django.core.validators import MaxLengthValidator
import datetime



class StaffRegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    phone_number = forms.CharField(label='電話號碼', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='地址', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_number = forms.CharField(label='身分證字號', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, initial='Female', widget=forms.Select(attrs={'class': 'form-control'}))
    
    birth_date = forms.DateField(label='生日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
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
    user_type = forms.ChoiceField(label='Staff Type', choices=USER_TYPE_CHOICES, initial='Crew - TA', widget=forms.Select(attrs={'class': 'form-control'}))
    
    CLASS_CHOISE = (
        ('2023A', '2023A'),
        ('2023B', '2023B'),
        ('2023C', '2023C'),
        ('2023D', '2023D'),
        ('2023E', '2023E'),
    )
    angel_class = forms.ChoiceField(label='CLASS of', choices=CLASS_CHOISE, initial='2023A', widget=forms.Select(attrs={'class': 'form-control'}))
    
    times = forms.IntegerField(label='時數', initial=0, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(StaffRegisterUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'