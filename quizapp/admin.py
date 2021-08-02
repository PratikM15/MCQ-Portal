from django.contrib import admin
from quizapp.models import *

models_list = [Question, StudentResponse, Test, Profile] 
admin.site.register(models_list)