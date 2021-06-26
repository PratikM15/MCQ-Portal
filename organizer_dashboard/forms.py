from django.forms import ModelForm
from quizapp.models import Question
from django import forms

class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question','choice1','choice2','choice3','choice4','answer']
