from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


from .forms import UserView,ProfileView


def Users(request):
    if request.method=="POST":
        user=UserView(request.POST)
        profile=ProfileView(request.POST,request.FILES)
        if user.is_valid() and profile.is_valid():
            Users= user.save(commit=False)
            Users.set_password(user.cleaned_data['password'])
            Users.save()

            profile= profile.save(commit=False)
            profile.user = Users
            profile.save()
            return redirect("login")
    else:
        User=UserView()
        Profile=ProfileView()
        return render(request,'reg.html',{'user':User,'profile':Profile})



from apps.appliances.models  import Appliance
from datetime import timedelta,date
@login_required
def main(request):
    app=Appliance.objects.order_by("Purchase_Date")
    total=app.count()
    today=date.today()
    ex=0
    ac=0
    soon=0
    for i in app:
            i.delta=i.Purchase_Date+timedelta(days=3)
            i.days=(today-i.Purchase_Date).days
            i.status='Expired' if i.days>=3 else "Active"
            i.time=(i.delta-today).days
            

            if i.days>=3:
                ex+=1
            else:
                ac+=1
            
            if i.time==1 :
                soon+=1

            i.ex_soon=f"{i.Product} Warranty Expiring in {i.time} days" if i.time==1 else ""
        
            
    return render(request,"main.html",{"app":app,'total':total,'ex':ex,'ac':ac,'soon':soon})

    
        

def login(request):
    if request.method=="POST":
        get_username=request.POST.get('username')
        get_password=request.POST.get('password')
        user=authenticate(request,username=get_username,password=get_password)
        if user is not None:
            auth_login(request,user)
            return redirect('main')

    return render(request,"login.html")

def logout(request):
    auth_logout(request)
    return redirect('login')



def index(request):
    return render(request,'index.html')

def files(request):
    return render(request,'files.html')
