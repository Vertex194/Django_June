# Register your models here.
from django.contrib import admin
from .models import TimeSlot, Reservation

admin.site.register(TimeSlot)
admin.site.register(Reservation)