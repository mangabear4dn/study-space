from django.contrib import admin
from .models import Reservation, Space


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    """AdminClass for Spaces"""
    list_filter = ['type', 'max_capacity']
    list_display = ['name', 'max_capacity', 'type', 'available_tech']
    search_fields = ['name']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """AdminClass for Reservations"""
    list_filter = ['start', 'space__type', 'snacks_discount']
    list_display = ['start', 'username', 'space', 'snacks_discount']
    search_fields = ['username']
