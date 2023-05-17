from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta, timezone

class Flight(models.Model):
    flight_id = models.CharField(default='FLID202500', max_length=20, unique=True)
    flight_date = models.DateField(default='2020-12-20')
    etd = models.TimeField()
    
    AIRPLANE_CHOICES = (
        ('Boeing', 'Boeing'),
        ('Airbus', 'Airbus'),
    )
    airplane = models.CharField(max_length=20, choices=AIRPLANE_CHOICES, default='Boeing')
    
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
    aircraft_type = models.CharField(max_length=20, choices=AIRCRAFT_TYPE_CHOICES, default='777-300ER')
    
    # 以下資料來源：民航局
    # B-162xx：A321-200
    # B-163xx：A330-200（B-1631x）、A330-300（B-16331～B-16340）
    # B-167xx：777-300ER/777-300ERSF（B-16701～B-16740）、777F（B-16781～B-16790）
    # B-1788x：787-9 Dreamliner
    # B-178xx：787-10 Dreamliner
    # https://zh.wikipedia.org/zh-hant/長榮航空#機隊編號
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
    ship_no = models.CharField(max_length=20, choices=SHIP_NO_CHOICES, default='B16703')
    
    flt_no = models.CharField(max_length=15)
    
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
    code_share = models.CharField(max_length=50, choices=CODE_SHARE_CHOICES, default='All Nippon Airways - NH')
    
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
    etd_airport = models.CharField(max_length=10, choices=AIRPORT_CHOICES, default='TPE')
    eta_airport = models.CharField(max_length=10, choices=AIRPORT_CHOICES, default='TPE')
    
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
    etd_utc = models.CharField(max_length=10, choices=UTC_CHOICES, default='UTC+8')
    eta_utc = models.CharField(max_length=10, choices=UTC_CHOICES, default='UTC+8')
    
    eta = models.DateTimeField(null=True, blank=True)
    
    # schedule_hr = models.DateTimeField(null=True, blank=True)
    schedule_hr_h = models.IntegerField(default=0)
    schedule_hr_m = models.IntegerField(default=0)
    
    fdp_hr_h = models.IntegerField(default=0)
    fdp_hr_m = models.IntegerField(default=0)
    
    RL_PL_SB = models.IntegerField(default=0)
    PE = models.IntegerField(default=0)
    EY = models.IntegerField(default=0)
    
    RL_PL_SB_booked = models.IntegerField(default=0)
    PE_booked = models.IntegerField(default=0)
    EY_booked = models.IntegerField(default=0)
    
    CHD = models.IntegerField(default=0)
    INF = models.IntegerField(default=0)
    
    crew_members = models.IntegerField(default=0)
    crew_assigned = models.IntegerField(default=0)
    
    # @property
    # def crew_members(self):
    #     return (self.RL_PL_SB + self.PE + self.EY) / 30 + 1
    
    # departure_location = models.CharField(max_length=100)
    # arrival_location = models.CharField(max_length=100)
    # flight_duration = models.DurationField()
    # date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
@receiver(pre_save, sender=Flight)
def calculate_eta(sender, instance, **kwargs):
    # Get the ETD and flight duration from the instance
    dep_time = instance.etd
    dep_utc = int(instance.etd_utc)
    arr_utc = int(instance.eta_utc)
    # flight_duration = instance.schedule_hr.total_seconds()
    
    now_utc = arr_utc - dep_utc
    if now_utc < 0:
        dep_time = dep_time - timedelta(hours=abs(now_utc))
    else:
        dep_time = dep_time + timedelta(hours=abs(now_utc))
        
    # Calculate the ETA
    eta = dep_time + timedelta(hours=instance.schedule_hr_h, minutes=instance.schedule_hr_m)
    
    # Set the ETA
    instance.eta = eta