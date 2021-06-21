from django.urls import path
from . import views

urlpatterns = [
    path('',views.organizer_dashboard,name='o_dashboard'),
    path('organizer_login',views.organizer_login,name='organizer_login'),
    path('organizer_registration',views.organizer_registration,name='organizer_registration'),
    path('o_logout',views.o_logout,name='o_logout'),

]