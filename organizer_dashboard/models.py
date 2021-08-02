from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Batch(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class BatchStudent(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return batch.name + student.username