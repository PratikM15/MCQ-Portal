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
        profile = Profile(user=myuser, is_user=True, is_organizer=False)
        profile.save()
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

@login_required(login_url='login_page')
def userProfile(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        name = request.POST["name"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        state = request.POST["state"]
        zipcode = request.POST["zip"]
        profession = request.POST["profession"]
        domain = request.POST["domain"]
        company = request.POST["company"]
        experience = request.POST["experience"]
        profile.name = name
        profile.address1 = address1
        profile.address2 = address2
        profile.city = city
        profile.state = state
        profile.zip = zipcode
        profile.profession = profession
        profile.domain = domain
        profile.company = company
        profile.experience = experience
        profile.save()
        return redirect("user-profile")
    context = {"profile":profile, "user":user}
    return render(request, 'quizapp/userProfile.html', context)


def home(request):
    try:
        username = request.user
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except:
        profile = None
    tests = Test.objects.all()
    context = {'tests':tests, 'profile': profile}
    # context = {'tests':tests}

    
    return render(request,'index.html', context)

@login_required(login_url='login_page')
def register(request, category):
    if request.method == 'POST':
        username = request.user
        user = User.objects.get(username=username)
        return redirect('questionportal', category)
    return render(request,'start.html', {'category':category})

@login_required(login_url='login_page')
def questionportal(request, category):
    username = request.user
    user = User.objects.get(username=username)
    test = Test.objects.get(category=category)
    questions = Question.objects.filter(test=test)
    student = Student(user=user, test=test, score=0)
    student.save()
    context = {'questions':questions, 'category':category, "time":test.test_time, "student":student}
    return render(request,'quiz.html',context=context)

    
def result(request, category):
    if request.method == "POST":
        student_id = request.POST["ext_id"]
        student = Student.objects.get(external_id=student_id)
        test = Test.objects.get(category=category)
        ques = Question.objects.filter(test=test)
        score = 0
        for que in ques:
            que_name = str(que.external_id)
            que_answer = request.POST.get(que_name, None)
            print(que_name, que_answer)
            if que_answer == que.answer:
                score += 1
        student.score = score
        student.completed = True
        student.save()
        return render(request,'dummy.html',{'score':score,'ques':ques, 'category':category})
    return redirect('home')

@login_required(login_url='login_page')
def results(request):
    username = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    tests = Student.objects.filter(user=user)
    context = {"responses": tests, 'profile':profile}
    return render(request, 'results.html', context)
    


