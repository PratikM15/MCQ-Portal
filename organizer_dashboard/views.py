from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def organizer_dashboard(request):
    return render(request,'organizer_dashboard/o_dashboard.html')

def organizer_registration(request):
    if request.method == 'POST':
        register_o_username = request.POST['register_o_username']
        register_o_email = request.POST['register_o_email']
        register_o_password = request.POST['register_o_password']

        if User.objects.filter(username=register_o_username).first():
            messages.warning(request,"This username is already taken")
            return redirect('home')
        if User.objects.filter(email=register_o_email):
            messages.warning(request,"Email is already registered")
            return redirect('home')

        #creating Organizer
        organizer = User.objects.create_user(username=register_o_username,email=register_o_email,password=register_o_password)
        organizer.save()
        messages.success(request,"Congratulations ! Organizer account has been Successfully created.")

        return redirect('organizer_login')
    return render(request,'organizer_registration.html')


def organizer_login(request):
    if request.method == 'POST':
        o_username = request.POST['ousername']
        o_password = request.POST['opassword']

        o_user = authenticate(username=o_username,password=o_password)
        
        if o_user is not None:
            login(request,o_user)
            messages.success(request,"You are Now Logged in as Organizer.")
            return redirect('o_dashboard')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')


    return render(request,'organizer_Login.html')