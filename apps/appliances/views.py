from django.shortcuts import render,HttpResponse
from .forms import Appliance_form

def apliance(request):
    if request.method=='POST':
        a_form=Appliance_form(request.POST)
        a_form.save()
        return HttpResponse('saved')
    else:
        a_form=Appliance_form()
    return render(request,'appliance.html',{'form':a_form})



    

