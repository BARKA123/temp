
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profile'),
    path('', views.contact, name='contact'),
    path('', views.newsletter, name='newsletter'),
    path('', views.dossiers, name='dossiers')
]

