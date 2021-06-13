from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .models import *

def home(request):
    return render(request,'index.html')

def register(request, category):
    if request.method == 'POST':
        name = request.POST["student"]
        return redirect('questionportal', category, name)
    return render(request,'start.html', {'category':category})


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