from django.contrib import admin
from django.urls import path
from . import views
#from mainapp import views
import os

urlpatterns = [
    path('register',views.register, name='register'),
]