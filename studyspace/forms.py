from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """This ir the form for regular user to make a registration"""
    class Meta:
        """Meta"""
        model = Reservation
        fields = ['username', 'start', 'space', 'snacks_discount']
