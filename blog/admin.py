# Register your models here.
from django.contrib import admin
from .models import TimeSlot, Reservation, Profile

admin.site.register(TimeSlot)
admin.site.register(Reservation)
admin.site.register(Profile)