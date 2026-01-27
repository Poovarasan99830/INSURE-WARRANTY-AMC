from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
  
from .forms import APPLIANCE

def Appliances(request):
    if request.method=="POST":
        products=APPLIANCE(request.POST)
        if products.is_valid():
            products.save()
            return HttpResponse('Success')
        return render(request,"appliance.html",{'products':products})
     
        
    else:
        products=APPLIANCE()
        return render(request,"appliance.html",{'products':products})
     


