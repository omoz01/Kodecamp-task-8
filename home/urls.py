from django.urls import path
from .views import index, about, contact, services 


app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]