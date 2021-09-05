from django.urls import path
from . import views

urlpatterns = [
    path('',views.organizer_dashboard,name='o_dashboard'),
    path('organizer_login',views.organizer_login,name='organizer_login'),
    path('organizer_registration',views.organizer_registration,name='organizer_registration'),
    path('o_logout',views.o_logout,name='o_logout'),
    path('addtest',views.addtest,name='addtest'),
    path('edit-test/<str:id>', views.editTest, name="edit-test"),
    path('delete-test/<str:id>', views.deleteTest, name="delete-test"),
    path('addQuestions',views.addQuestions,name='addQuestions'),
    path('edit-question/<str:id>', views.editQuestion, name="edit-question"),
    path('delete-question/<str:id>', views.deleteQuestion, name="delete-question"),
    path('user-results',views.user_results,name='user-results'),
    path('batch', views.add_batch, name='batch'),
    path('register-batch/<str:id>', views.register_batch, name='register-batch'),
    path('add-video', views.addVideo, name="add-video"),
    path('update-video/<str:id>', views.updateVideo, name="update-video"),
    path('delete-video/<str:id>', views.deleteVideo, name="delete-video"),

]