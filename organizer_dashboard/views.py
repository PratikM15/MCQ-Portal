from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from quizapp.models import *
from .models import *
from .forms import AddQuestionForm
# Create your views here.

def organizer_dashboard(request):
    username = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {'profile':profile}
    if profile.is_organizer:
        return render(request,'organizer_dashboard/o_dashboard.html', context)
    return redirect('organizer_registration')

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
        profile = Profile(user=organizer, is_organizer=True)
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
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        desc = request.POST['desc']
        time = request.POST['time']
        testInfo  = Test(user=user, name=name, category=category, description=desc, test_time=time)
        testInfo.save() 
        message = "Test for {} category created successfully.".format(category)
        messages.success(request, message)
        return redirect('addtest')
    tests = Test.objects.filter(user=user)
    context = {"tests":tests, 'profile':profile}
    return render(request,'organizer_dashboard/addtestForm.html', context)

def editTest(request, id):
    username = request.user
    user = User.objects.get(username=username)
    test = Test.objects.get(external_id=id)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        desc = request.POST['desc']
        time = request.POST['time']
        test.name = name
        test.category = category
        test.description = desc
        test.test_time = time
        test.save()
        message = "Test Edited successfully."
        messages.success(request, message)
        return redirect('addtest')
    tests = Test.objects.filter(user=user)
    context = {"tests":tests, 'test':test, 'profile':profile}
    return render(request,'organizer_dashboard/addtestForm.html', context)

def deleteTest(request, id):
    test = Test.objects.get(external_id=id)
    test.delete()
    message = "Test Deleted successfully."
    messages.success(request, message)
    return redirect('addtest')
    
def addQuestions(request):
    username = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        question = request.POST['question']
        choice1 = request.POST['choice1']
        choice2 = request.POST['choice2']
        choice3 = request.POST['choice3']
        choice4 = request.POST['choice4']
        correctchoice = request.POST['correctchoice']
        category = request.POST['category']
        level = request.POST['level']
        test = Test.objects.get(external_id=category)
        create_question = Question(test=test, question=question, choice1=choice1, choice2=choice2, 
        choice3=choice3, choice4=choice4, answer=correctchoice, level=level)
        create_question.save()
        msg2 = "Question added to question bank."
        messages.success(request, msg2)
        return redirect('addQuestions')
    tests = Test.objects.filter(user=user)
    questions = []
    for test in tests:
        questions += list(Question.objects.filter(test=test))
    context = { 'tests':tests, 'questions':questions, 'profile':profile}
    return render(request,'organizer_dashboard/addQuestionForm.html',context=context)

def editQuestion(request, id):
    question = Question.objects.get(external_id=id)
    username = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        question = request.POST['question']
        choice1 = request.POST['choice1']
        choice2 = request.POST['choice2']
        choice3 = request.POST['choice3']
        choice4 = request.POST['choice4']
        correctchoice = request.POST['correctchoice']
        category = request.POST['category']
        level = request.POST['level']
        test = Test.objects.get(external_id=category)
        question.question = question
        question.choice1 = choice1
        question.choice2 = choice2
        question.choice3 = choice3
        question.choice4 = choice4
        question.answer = correctchoice
        question.test = test
        question.level = level
        question.save()
        msg2 = "Question Updated Successfully."
        messages.success(request, msg2)
        return redirect('addQuestions')
    tests = Test.objects.filter(user=user)
    questions = []
    for test in tests:
        questions += list(Question.objects.filter(test=test))
    context = { 'tests':tests, 'questions':questions, 'profile':profile, 'question':question}
    return render(request,'organizer_dashboard/addQuestionForm.html',context=context)

def deleteQuestion(request, id):
    question = Question.objects.get(external_id=id)
    question.delete()
    msg2 = "Question Deleted Successfully."
    messages.success(request, msg2)
    return redirect('addQuestions')

def user_results(request):
    username = request.user
    user = User.objects.get(username=username)
    tests = Test.objects.filter(user=user)
    students = []
    for test in tests:
        students += list(Student.objects.filter(test=test))
    context = {'students': students}
    return render(request, 'organizer_dashboard/results.html', context)

def add_batch(request):
    username = request.user
    user = User.objects.get(username=username)
    if request.method == "POST":
        name = request.POST["name"]
        size = request.POST['size']
        batch = Batch(name=name, size=size, organizer=user)
        batch.save()
        return redirect('batch')
    batches = Batch.objects.filter(organizer=user)
    context = {'batches':batches}
    return render(request, 'organizer_dashboard/batch.html', context)

def register_batch(request, id):
    username = request.user
    user = User.objects.get(username=username)
    batch = Batch.objects.get(external_id=id)
    num = len(BatchStudent.objects.all())
    batchStudent = BatchStudent.objects.filter(batch=batch).filter(student=user)
    if batchStudent:
        messages.error(request, "Already Registered for this batch.")
        return redirect('home')
    if num < int(batch.size):
        batchStudent = BatchStudent(student=user, batch=batch)
        batchStudent.save()
        msg = "Successfully Registered For Batch: "+ batch.name
        messages.success(request, msg)
        return redirect('home')
    else:
        messages.error(request, "Batch Full")
        return redirect('home')

def addVideo(request):
    username = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        newurl = url.split('=')
        newurl = "https://www.youtube.com/embed/" + newurl[-1]
        description = request.POST['description']
        video = Video(organizer=user, title=title, description=description, url=newurl)
        video.save()
        msg2 = "Video Added Successfully."
        messages.success(request, msg2)
        return redirect('add-video')
    videos = Video.objects.filter(organizer=user)
    context = {'videos':videos, 'profile':profile}
    return render(request,'organizer_dashboard/addVideos.html',context=context)

def updateVideo(request, id):
    video = Video.objects.get(external_id=id)
    username = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        newurl = url.split('=')
        newurl = "https://www.youtube.com/embed/"+newurl[-1]
        description = request.POST['description']
        video.title = title
        video.description = description
        video.url = newurl
        video.save()
        msg2 = "Video Updated Successfully."
        messages.success(request, msg2)
        return redirect('add-video')
    videos = Video.objects.filter(organizer=user)
    context = {'videos':videos, 'profile':profile, 'video':video}
    return render(request,'organizer_dashboard/addVideos.html',context=context)

def deleteVideo(request, id):
    video = Video.objects.get(external_id=id)
    video.delete()
    msg2 = "Video Deleted Successfully."
    messages.success(request, msg2)
    return redirect('add-video')