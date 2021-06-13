from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/<str:category>', views.register, name='register'),
    path('questionportal/<str:category>/<str:name>',views.questionportal,name='questionportal'),
    path('results/<str:category>/<str:name>',views.results,name='results'),
]