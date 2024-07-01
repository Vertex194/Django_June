from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
import logging

logging = logging.getLogger(__name__)

def make_reservation(request):
    return render(request,'blog/make_reservation.html')

def about(request):
    return render(request,'blog/about.html')

def home(request):
    return render(request,'blog/index.html')