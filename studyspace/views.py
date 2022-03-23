from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from django.template import loader
from .models import Space, Reservation
from .forms import ReservationForm


def get_home(request):
    """Get home page"""
    return render(request, 'studyspace/index.html')


def get_spaces_list(request):
    """Reference: https://docs.djangoproject.com/en/4.0/intro/tutorial03/"""
    spaces_list = Space.objects.order_by('name')
    template = loader.get_template('studyspace/spaces.html')
    context = {
        'spaces_list': spaces_list,
    }
    return HttpResponse(template.render(context, request))


def get_my_profile(request):
    """Display all my reservations"""
    reservations = Reservation.objects.all().order_by('start')
    template = loader.get_template('studyspace/profile.html')
    context = {
        'reservations': reservations,
    }
    return HttpResponse(template.render(context, request))


def reserve(request):
    """Make a reservation
    references: https://realpython.com/django-redirects/
    """
    form = ReservationForm(request.POST)
    template = loader.get_template('studyspace/reserve.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
