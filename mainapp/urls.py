from django.contrib import admin
from django.urls import path
from . import views
#from mainapp import views
import os

urlpatterns = [
    path('',views.Index, name='Index'),
    path('senddata',views.senddata),
    path('discover/',views.discover),
    path('register/',views.register),
    path('register/reg_done/',views.reg_done),
    path('login/',views.login),
    path('discover/send_mail_user/',views.send_mail_user),
    path('login/log_done/',views.log_done),
    #path('sorry/',views.sorry),
]
