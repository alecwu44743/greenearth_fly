from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.core.mail import send_mail
from .models import UserProfile

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, "There Was An Error!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Sign Out Successful")
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            id_number = form.cleaned_data['id_number']
            gender = form.cleaned_data['gender']
            birth_date = form.cleaned_data['birth_date']
            user_type = form.cleaned_data['user_type']
            miles = form.cleaned_data['miles']
            level = form.cleaned_data['level']
            user = authenticate(username=username, password = password)
            
            if user is not None:
                login(request, user)
                user_profile, _ = UserProfile.objects.get_or_create(user=user)
                user_profile.phone_number = phone_number
                user_profile.address = address
                user_profile.id_number = id_number
                user_profile.gender = gender
                user_profile.birth_date = birth_date
                user_profile.user_type = user_type
                user_profile.miles = miles
                user_profile.level = level
                user_profile.save()
                messages.success(request, "Sign Up Completed!")
                return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form':form,
    })