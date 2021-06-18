from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # check input
        if User.objects.filter(username=username).first():
            messages.warning(request, "This username is already taken")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.warning(request,"Email already registered")
            return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.save()
        messages.success(request,"Congratulations ! Exammer account has been Successfully created.")
        return redirect('login_page')
    
    return render(request, 'userRegister.html')
    
    

def login_page(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged In!")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')
    
    return render(request,'login.html')

    
@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')








def home(request):
    return render(request,'index.html')

@login_required(login_url='login_page')
def register(request, category):
    if request.method == 'POST':
        name = request.POST["student"]
        return redirect('questionportal', category, name)
    return render(request,'start.html', {'category':category})

@login_required(login_url='login_page')
def questionportal(request, category, name):
    test = Test.objects.get(category=category)
    questions = Question.objects.filter(test=test)
    context = {'questions':questions, "name":name, 'category':category}
    return render(request,'quiz.html',context=context)

    
def results(request, category, name):
    if request.method == "POST":
        test = Test.objects.get(category=category)
        ques = Question.objects.filter(test=test)
        score = 0
        for que in ques:
            que_name = str(que.external_id)
            que_answer = request.POST.get(que_name, None)
            print(que_name, que_answer)
            if que_answer == que.answer:
                score += 1
        return render(request,'dummy.html',{'score':score,'ques':ques, 'name':name, 'category':category})
    return redirect('home')


