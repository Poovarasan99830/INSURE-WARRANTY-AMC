from django.shortcuts import render,redirect,HttpResponse
from .forms import registerform,userfrom

# Create your views here.
def user_register(request):
    if request.method=='POST':
        u_form=userfrom(request.POST)
        r_form=registerform(request.POST)
        if u_form.is_valid and r_form.is_valid():
            user=u_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile=r_form.save(commit=False)
            profile.user=user
            profile.save()
            return redirect('login_user')
    else:
        u_form=userfrom()
        r_form=registerform()
    return render(request,'register.html',{'userform':u_form,'regform':r_form})

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method=='POST':
        get_username=request.POST.get('username')
        get_password=request.POST.get('password')
        user=authenticate(request,username=get_username,password=get_password)

        if user:
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse('your password or gmail is wrong')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_user')

def main(request):
    return render(request,'main.html')
