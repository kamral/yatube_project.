
from django.urls import path
from .views import  index,groups

urlpatterns=[
    path('',index, name='index'),
    path('group/<slug:slug>/', groups, name='group')

]