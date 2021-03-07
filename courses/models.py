from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from users.models import CustomUser
# Create your models here.
class Course (models.Model):
    COURSE_TYPE = (
        ('E', 'Eassy'),
        ('M', 'Medium'),
        ('A', 'Advanced'),
        ('D', 'Difficult'),
    )

    name = models.CharField(max_length = 60, unique = True)
    type = models.CharField(max_length=1,choices=COURSE_TYPE)
    description = models.TextField(max_length=400)
    duration = models.IntegerField()
    creator = ForeignKey('users.CustomUser',on_delete=CASCADE)
    rating = models.IntegerField(null= True)
    pub = models.DateField(auto_now=True)
    logo = models.ImageField()
    colour = models.CharField(max_length=6)

class Video (models.Model):
    name = models.CharField(max_length = 60)
    video = models.FileField()
    description = models.TextField(max_length=400)
    views = models.IntegerField(null = True)
    duration = models.IntegerField()
    course = ForeignKey('Course', on_delete=CASCADE)

class Comment (models.Model):
    user = ForeignKey('users.CustomUser',on_delete=CASCADE)
    video = ForeignKey('Video', on_delete=CASCADE)
    pub = models.DateField(auto_now=True)
    hour = models.TimeField(auto_now=True)
    text = models.TextField(max_length= 400)
class Seem (models.Model):
    user = ForeignKey('users.CustomUser',on_delete=CASCADE)
    Video = ForeignKey('Course',on_delete=CASCADE)
    check = models.BooleanField(auto_created=False)
