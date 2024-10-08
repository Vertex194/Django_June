from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from.models import Reservation,TimeSlot
from.forms import ReservationForm
import logging

logging = logging.getLogger(__name__)

def index(request):
    return render(request,'blog/index.html')

def make_reservation(request):    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            
            user_email = request.user.email
            reservation_date = reservation.time_slot.date
            reservation_time = reservation.time_slot.start_time

            email_subject = 'Reservation Confirmation'
            email_message = f'親愛的 {request.user.username} 您好預約已成功。 \n日期：{reservation_date}\n時間：{reservation_time}\n\n感謝您的預約!'
            try:
                send_mail(
                    email_subject, 
                    email_message, 
                    settings.DEFAULT_FROM_EMAIL, 
                    [user_email], 
                    fail_silently=False
                    )
                logging.info(f"Email sent successfully to {user_email}")
                email_sent = 1
            except Exception as e:
                logging.error(f"Email sendding email: {e}")
                email_sent = 0
            return redirect('reservation_success',email_sent=email_sent)
    else:
        form = ReservationForm()
        
    time_slots = TimeSlot.objects.all()
    return render(request,'blog/make_reservation.html', {'form': form, 'time_slots': time_slots})

def reservation_success(request,email_sent):
    email_sent = bool(int(email_sent))
    return render(request,'blog/reservation_success.html', {'email_sent': email_sent})

def about(request):
    return render(request,'blog/about.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import ProfileForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.email = profile_form.cleaned_data.get('email')
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request,'account/register.html', {'form': form,'profile_form': profile_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('make_reservation')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../make_reservation')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html', {'form': form})
