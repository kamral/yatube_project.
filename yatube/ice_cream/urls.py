from django.urls import path
from .views import index, ice_cream,ice_cream_detail


urlpatterns=[
    path('', index, name='index'),
    path('ice_cream_list/', ice_cream, name='ice_cream'),
    path('ice_cream/<int:pk>/', ice_cream_detail, name='ice_cream_detail')
]