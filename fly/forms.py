from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.core.validators import MaxLengthValidator
import datetime
from datetime import datetime, timedelta, timezone
import datetime
from django.utils import timezone
from .models import Flight


class NewFlightsForm(forms.ModelForm):
    last_flight = Flight.objects.last()
    last_id = 2025000
    if last_flight is not None:
        last_id = int(last_flight.id) + 2025000
    
    flight_id = forms.CharField(label='Flight ID', max_length=10, initial='FID' + str(last_id), widget=forms.TextInput(attrs={'class': 'form-control'}), disabled=True)
    flight_date = forms.DateField(label='Flight Date', initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    etd = forms.TimeField(label='Flight Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'HH:MM'}))
    
    AIRPLANE_CHOICES = (
        ('Boeing', 'Boeing'),
        ('Airbus', 'Airbus'),
    )
    airplane = forms.CharField(label='Airplane', widget=forms.Select(choices=AIRPLANE_CHOICES, attrs={'class': 'form-control'}))
    
    AIRCRAFT_TYPE_CHOICES = (
        ('A321-200', 'A321-200'),
        ('A330-200', 'A330-200'),
        ('A330-300', 'A330-300'),
        ('777-300ER', '777-300ER'),
        ('777-300ERSF', '777-300ERSF'),
        ('777F', '777F'),
        ('787-9 Dreamliner', '787-9 Dreamliner'),
        ('787-10 Dreamliner', '787-10 Dreamliner'),
    )
    aircraft_type = forms.CharField(label='Aircraft Type', widget=forms.Select(choices=AIRCRAFT_TYPE_CHOICES, attrs={'class': 'form-control'}))
    
    SHIP_NO_CHOICES = (
        ('B16206', 'A321-200 B16206'), # A321-200
        ('B16310', 'A330-200 B16310'), # A330-200
        ('B16311', 'A330-200 B16311'),
        ('B16312', 'A330-200 B16312'),
        ('B16331', 'A330-300 B16331'), # A330-300
        ('B16332', 'A330-300 B16332'),
        ('B16333', 'A330-300 B16333'),
        ('B16703', '777-300ER B16703'), # 777-300ER
        ('B16705', '777-300ER B16705'),
        ('B16706', '777-300ER B16706'),
        ('B16701', '777-300ERSF B16701'), # 777-300ERSF
        ('B16740', '777-300ERSF B16740'),
        ('B16781', '777F B16781'), # 777F
        ('B16782', '777F B16782'),
        ('B16783', '777F B16783'),
        ('B17881', '787-9 Dreamliner B17881'), # 787-9 Dreamliner
        ('B17882', '787-9 Dreamliner B17882'),
        ('B17883', '787-9 Dreamliner B17883'),
        ('B17801', '787-10 Dreamliner B17801'), # 787-10 Dreamliner
        ('B17802', '787-10 Dreamliner B17802'),
        ('B17803', '787-10 Dreamliner B17803'),
    )
    ship_no = forms.CharField(label='Ship No.', widget=forms.Select(choices=SHIP_NO_CHOICES, attrs={'class': 'form-control'}))
    
    flt_no = forms.CharField(label='Flight No.', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    CODE_SHARE_CHOICES = (
        ('All Nippon Airways - NH', 'All Nippon Airways - NH'),
        ('Bangkok Airways - PG', 'Bangkok Airways - PG'),
        ('Air China - CA', 'Air China - CA'),
        ('Hainan Airlines - HU', 'Hainan Airlines - HU'),
        ('Asiana Airlines - OZ', 'Asiana Airlines - OZ'),
        ('Shandong Airlines - SC', 'Shandong Airlines - SC'),
        ('Hong Kong Airlines - HX', 'Hong Kong Airlines - HX'),
        ('United Airlines - UA', 'United Airlines - UA'),
        ('Singapore Airlines - SQ', 'Singapore Airlines - SQ'),
        ('Turkish Airlines - TK', 'Turkish Airlines - TK'),
        ('Air India - AI', 'Air India - AI'),
        ('Air Canada - AC', 'Air Canada - AC'),
        ('Shenzhen Airlines - ZH', 'Shenzhen Airlines - ZH'),
        ('Avianca Airlines - AV', 'Avianca Airlines - AV'),
        ('Thai Airlines - TG', 'Thai Airlines - TG'),
        ('Copa Airlines - CM', 'Copa Airlines - CM'),
        ('Juneyao Airlines - HO', 'Juneyao Airlines - HO'),
        ('Air New Zealand - NZ', 'Air New Zealand - NZ'),
    )
    code_share = forms.CharField(label='Code Share', widget=forms.Select(choices=CODE_SHARE_CHOICES, attrs={'class': 'form-control'}))
    
    AIRPORT_CHOICES = (
        ('TPE', 'TPE - Taiwan Taoyuan International Airport'),
        ('HKG', 'HKG - Hong Kong International Airport'),
        ('LAX', 'LAX - Los Angeles International Airport'),
        ('SFO', 'SFO - San Francisco International Airport'),
        ('JFK', 'JFK - John F. Kennedy International Airport'),
        ('LHR', 'LHR - London Heathrow Airport'),
        ('SEA', 'SEA - Seattle-Tacoma International Airport'),
        ('YVR', 'YVR - Vancouver International Airport'),
        ('YYZ', 'YYZ - Toronto Pearson International Airport'),
        ('IAH', 'IAH - George Bush Intercontinental Airport'),
        ('BKK', 'BKK - Suvarnabhumi Airport'),
        ('NRT', 'NRT - Narita International Airport'),
        ('ICN', 'ICN - Incheon International Airport'),
        ('PVG', 'PVG - Shanghai Pudong International Airport'),
        ('HND', 'HND - Tokyo Haneda Airport'),
        ('CDG', 'CDG - Charles de Gaulle Airport'),
        ('AMS', 'AMS - Amsterdam Airport Schiphol'),
        ('SIN', 'SIN - Singapore Changi Airport'),
        ('ORD', 'ORD - O\'Hare International Airport'),
        ('MUC', 'MUC - Munich Airport'),
        ('CAN', 'CAN - Guangzhou Baiyun International Airport'),
        ('SCL', 'SCL - Santiago International Airport'),
        ('BNE', 'BNE - Brisbane Airport'),
    )
    etd_airport = forms.CharField(label='Departure Airport', initial='TPE', widget=forms.Select(choices=AIRPORT_CHOICES, attrs={'class': 'form-control'}))
    eta_airport = forms.CharField(label='Arrival Airport', initial='LAX', widget=forms.Select(choices=AIRPORT_CHOICES, attrs={'class': 'form-control'}))
    
    UTC_CHOICES = (
        ('+1', 'UTC+1'),
        ('+2', 'UTC+2'),
        ('+3', 'UTC+3'),
        ('+4', 'UTC+4'),
        ('+5', 'UTC+5'),
        ('+6', 'UTC+6'),
        ('+7', 'UTC+7'),
        ('+8', 'UTC+8'),
        ('+9', 'UTC+9'),
        ('+10', 'UTC+10'),
        ('+11', 'UTC+11'),
        ('+12', 'UTC+12'),
        ('-1', 'UTC-1'),
        ('-2', 'UTC-2'),
        ('-3', 'UTC-3'),
        ('-4', 'UTC-4'),
        ('-5', 'UTC-5'),
        ('-6', 'UTC-6'),
        ('-7', 'UTC-7'),
        ('-8', 'UTC-8'),
        ('-9', 'UTC-9'),
        ('-10', 'UTC-10'),
        ('-11', 'UTC-11'),
        ('-12', 'UTC-12'),
    )
    etd_utc = forms.CharField(label='Departure UTC', initial='+8', widget=forms.Select(choices=UTC_CHOICES, attrs={'class': 'form-control'}))
    eta_utc = forms.CharField(label='Arrival UTC', initial='-8', widget=forms.Select(choices=UTC_CHOICES, attrs={'class': 'form-control'}))
    
    # schedule_hr = forms.TimeField(
    #     input_formats=['%H:%M'],
    #     widget=forms.TimeInput(format='%H:%M', attrs={'class': 'form-control'})
    # )
    schedule_hr_h = forms.IntegerField(label='Schedule Hr (h)', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    schedule_hr_m = forms.IntegerField(label='Schedule Hr (m)', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    fdp_hr_h = forms.IntegerField(label='FDP Hr (h)', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fdp_hr_m = forms.IntegerField(label='FDP Hr (m)', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    RL_PL_SB = forms.IntegerField(label='RL/PL/SB', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    PE = forms.IntegerField(label='PE', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    EY = forms.IntegerField(label='EY', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    RL_PL_SB_booked = forms.IntegerField(label='RL/PL/SB Booked', initial=0, widget=forms.HiddenInput())
    PE_booked = forms.IntegerField(label='PE Booked', initial=0, widget=forms.HiddenInput())
    EY_booked = forms.IntegerField(label='EY Booked', initial=0, widget=forms.HiddenInput())
    
    CHD = forms.IntegerField(label='CHD', initial=0, widget=forms.HiddenInput())
    INF = forms.IntegerField(label='INF', initial=0, widget=forms.HiddenInput())
    
    crew_members = forms.IntegerField(label='Crew Members', initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Flight
        fields = ('flight_id', 'flt_no', 'flight_date', 'etd', 'schedule_hr_h', 'schedule_hr_m', 'airplane', 'aircraft_type', 'ship_no', 'code_share', 'etd_airport', 'eta_airport', 'etd_utc', 'eta_utc', 'fdp_hr_h', 'fdp_hr_m', 'RL_PL_SB', 'PE', 'EY', 'RL_PL_SB_booked', 'PE_booked', 'EY_booked', 'CHD', 'INF', 'crew_members')