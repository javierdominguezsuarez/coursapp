from courses.models import Comment, Course, Seem, Video
from django.contrib import admin

# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Seem)