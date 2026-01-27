
from django.contrib import admin
from django.urls import path



from apps.appliances import views
urlpatterns = [
    path('app/',views.Appliances,name='app')
]