from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    
    phone_number = forms.CharField(label='電話號碼', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='地址', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_number = forms.CharField(label='身分證字號', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, initial='Female', widget=forms.Select(attrs={'class': 'form-control'}))
    
    birth_date = forms.DateField(label='生日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    USER_TYPE_CHOICES = (
        ('Pessanger', 'Pessanger'),
        ('Crew', 'Crew'),
        ('Pilot', 'Pilot'),
        ('Office', 'Office'),
    )
    user_type = forms.ChoiceField(label='使用者類型', choices=USER_TYPE_CHOICES, initial='Pessanger', widget=forms.HiddenInput())
    
    miles = forms.IntegerField(label='里程', initial=0, widget=forms.HiddenInput())
    
    LEVEL_CHOICES = (
        ('Green', 'Green'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Diamond', 'Diamond'),
    )
    level = forms.ChoiceField(label='會員等級', choices=LEVEL_CHOICES, initial='Green', widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
            self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'