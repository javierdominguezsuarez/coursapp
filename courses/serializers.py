from django.db.models import fields
from rest_framework import serializers
from .models import *
class CourseSerilizer (serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','type','description','duration','creator','logo','colour']

class VideoSerilizer (serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name','video','description','duration','course']

class CommentSerilizer (serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user','video']

class SeemSerilizer (serializers.ModelSerializer):
    class Meta:
        model = Seem
        fields = ['video','user','check']