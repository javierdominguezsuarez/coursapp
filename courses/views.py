from courses.serializers import *
from courses.models import *
from rest_framework import viewsets
# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerilizer
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerilizer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizer
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerilizer
class SeemViewSet(viewsets.ModelViewSet):
    queryset = Seem.objects.all()
    serializer_class = SeemSerilizer