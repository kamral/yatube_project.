from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Главная страница')

def groups(request, any_slug):
    return HttpResponse(f'Группы {any_slug}')


