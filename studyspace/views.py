from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.template import loader
from .models import Space, Reservation


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
