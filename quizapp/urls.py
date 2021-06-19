from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/<str:category>', views.register, name='register'),
    path('questionportal/<str:category>',views.questionportal,name='questionportal'),
    path('result/<str:category>',views.result,name='result'),
    path('login',views.login_page,name='login_page'),
    path('register',views.register_page,name='register_page'),
    path('logout',views.logout_page,name='logout_page'),
    path('results',views.results,name='results'),
]