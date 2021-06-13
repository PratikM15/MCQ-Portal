from django.contrib import admin
from quizapp.models import *

models_list = [Question, StudentResponse, Test] 
admin.site.register(models_list)