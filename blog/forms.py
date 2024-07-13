from django import forms
from .models import Reservation, TimeSlot

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['time_slot', 'number_of_people']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_slot'].queryset = TimeSlot.objects.filter(available=True)