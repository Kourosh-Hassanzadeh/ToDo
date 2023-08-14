from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ToDo(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    done = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
