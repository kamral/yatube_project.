from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('главная страница')

def ice_cream(request):
    return HttpResponse('список мороженного')

def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')