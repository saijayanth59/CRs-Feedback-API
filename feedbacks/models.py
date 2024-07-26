from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    YEAR_CHOICES = [
        ("E1", "E1"),
        ("E2", "E2"),
        ("E3", "E3"),
        ("E4", "E4"),
    ]
    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    section = models.CharField(max_length=3) 


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    taken = models.BooleanField()
    remarks = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
