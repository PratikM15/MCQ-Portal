from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    test_time = models.CharField(max_length=3, default=None)
    

    def __str__(self):
        return self.category

class Student(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    score = models.CharField(max_length=3)
    completed = models.BooleanField(default=False)
    remaining_time = models.CharField(default="", max_length=3)

    def __str__(self):
        return self.name + " " + str(self.test.code)

class Question(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    question = models.CharField(max_length=500)
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=1)
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.question

class StudentResponse(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name + " " + str(self.test.code)

class Profile(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    address1 = models.CharField(max_length=500, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    zip = models.CharField(max_length=200, default="")
    profession = models.CharField(max_length=200, default="")
    domain = models.CharField(max_length=200, default="")
    company = models.CharField(max_length=200, default="")
    experience = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.user