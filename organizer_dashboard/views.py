from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from quizapp.models import *
from .forms import AddQuestionForm
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
        profile = Profile(user=organizer)
        profile.save()
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

def o_logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')

def addtest(request):
    username = request.user
    user = User.objects.get(username=username)
    if request.method == 'POST':
        category = request.POST['category']
        desc = request.POST['desc']
        time = request.POST['time']
        testInfo  = Test(user=user,category=category,description=desc,test_time=time)
        testInfo.save()
        message = "Test for {} category created successfully.".format(category)
        messages.success(request, message)
        return redirect('o_dashboard')
    tests = Test.objects.filter(user=user)
    context = {"tests":tests}
    return render(request,'organizer_dashboard/addtestForm.html', context)
    

def addQuestions(request):
    username = request.user
    user = User.objects.get(username=username)

    if request.method == 'POST':
        question = request.POST['question']
        choice1 = request.POST['choice1']
        choice2 = request.POST['choice2']
        choice3 = request.POST['choice3']
        choice4 = request.POST['choice4']
        correctchoice = request.POST['correctchoice']
        category = request.POST['category']
        test = Test.objects.get(external_id=category)
        create_question = Question(test=test, question=question,choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,answer=correctchoice)
        create_question.save()
        msg2 = "Question added to question bank."
        messages.success(request, msg2)
        return redirect('addQuestions')

    
    tests = Test.objects.filter(user=user)
    questions = []
    for test in tests:
        questions += list(Question.objects.filter(test=test))
    print(tests)
    context = { 'tests':tests, 'questions':questions}
    



    return render(request,'organizer_dashboard/addQuestionForm.html',context=context)