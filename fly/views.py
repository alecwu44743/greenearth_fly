from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import NewFlightsForm
from django.core.mail import send_mail
from .models import Flight


def newFlight(request):
    if request.method == 'POST':
        form = NewFlightsForm(request.POST)
        if form.is_valid():
            form.save()
            flight_id = form.cleaned_data['flight_id']
            flight_date = form.cleaned_data['flight_date']
            airplane = form.cleaned_data['airplane']
            aircraft = form.cleaned_data['aircraft']
            ship_no = form.cleaned_data['ship_no']
            flt_no = form.cleaned_data['flt_no']
            code_share = form.cleaned_data['code_share']
            etd_airport = form.cleaned_data['etd_airport']
            eta_airport = form.cleaned_data['eta_airport']
            etd_utc = form.cleaned_data['etd_utc']
            eta_utc = form.cleaned_data['eta_utc']
            etd = form.cleaned_data['etd']
            eta = form.cleaned_data['eta']
            # schedule_hr = form.cleaned_data['schedule_hr']
            schedule_hr_h = form.cleaned_data['schedule_hr_h']
            schedule_hr_m = form.cleaned_data['schedule_hr_m']
            fdp_hr_h = form.cleaned_data['fdp_hr_h']
            fdp_hr_m = form.cleaned_data['fdp_hr_m']
            RL_PL_SB = form.cleaned_data['RL_PL_SB']
            PE = form.cleaned_data['PE']
            EY = form.cleaned_data['EY']
            
            RL_PL_SB_booked = form.cleaned_data['RL_PL_SB_booked']
            PE_booked = form.cleaned_data['PE_booked']
            EY_booked = form.cleaned_data['EY_booked']
            
            CHD = form.cleaned_data['CHD']
            INF = form.cleaned_data['INF']
            crew_members = form.cleaned_data['crew_members']
            
            flight_profile, _ = Flight.objects.get_or_create(flight_id=flight_id)
            flight_profile.flight_date = flight_date
            flight_profile.airplane = airplane
            flight_profile.aircraft = aircraft
            flight_profile.ship_no = ship_no
            flight_profile.flt_no = flt_no
            flight_profile.code_share = code_share
            flight_profile.etd_airport = etd_airport
            flight_profile.eta_airport = eta_airport
            flight_profile.etd_utc = etd_utc
            flight_profile.eta_utc = eta_utc
            flight_profile.etd = etd
            # flight_profile.schedule_hr = schedule_hr
            flight_profile.eta = eta
            flight_profile.schedule_hr_h = schedule_hr_h
            flight_profile.schedule_hr_m = schedule_hr_m
            flight_profile.fdp_hr_h = fdp_hr_h
            flight_profile.fdp_hr_m = fdp_hr_m
            flight_profile.RL_PL_SB = RL_PL_SB
            flight_profile.PE = PE
            flight_profile.EY = EY
            flight_profile.RL_PL_SB_booked = RL_PL_SB_booked
            flight_profile.PE_booked = PE_booked
            flight_profile.EY_booked = EY_booked
            flight_profile.CHD = CHD
            flight_profile.INF = INF
            flight_profile.crew_members = crew_members
            flight_profile.save()
            
            messages.success(request, "Flight Added!")
            return redirect('myGreenEarth')
    else:
        form = NewFlightsForm()
        
    return render(request, 'authenticate/newFlight.html', {
        'form': form,
    })