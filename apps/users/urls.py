

from django.contrib import admin
from django.urls import path

from apps.users import views




urlpatterns =[ 
    path('user/',views.Users,name="user"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout'),
    path('main/',views.main,name="main"),]

   