from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse

from .forms import Userregistration
from .models import User,Login
from django.http import HttpResponse, HttpResponseRedirect


def home(request):


        return render(request, 'home.html')
def register(request):
    if request.method=='POST':
        fm=Userregistration(data=request.POST,files=request.FILES)

        if request.method=='POST' or fm.is_valid():
            image = request.FILES.get('image')
            cn=request.POST.get('company')
            un=request.POST.get('username')
            pwd=request.POST.get('password')
            em=request.POST.get('email')
            fn=request.POST.get('firstname')
            ln=request.POST.get('lastname')
            address=request.POST.get('address')
            city=request.POST.get('city')
            country=request.POST.get('country')
            postal_code=request.POST.get('postal_code')
            about_me=request.POST.get('about_me')
            #pw=fm.cleaned_data['password']
            #copw=fm.cleaned_data['confirmpassword']

            reg=User(image=image,company=cn, username=un,password=pwd,email=em,firstname=fn,lastname=ln,address=address,city=city,country=country,postal_code=postal_code,about_me=about_me)

            reg.save()
            fm=Userregistration()
    else:
        fm = Userregistration()

    stud=User.objects.all()

    return render(request,'loggin.html',{'form':fm,'stu':stud})


def loggin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        fm = authenticate(username=username, password=password)
        if fm:
            if fm.is_active:
                login(request,fm)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'loggin.html', {})