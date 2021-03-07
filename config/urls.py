"""coursApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from courses.views import *
from django.conf.urls import include
from users.views import*
from django.contrib import admin
from rest_framework import routers
from django.urls import path
routerDos = routers.SimpleRouter()
routerDos.register('register', RegisterViewSet, basename='auth_register')
routerTres = routers.SimpleRouter()
routerTres.register('login',LoginViewSet, basename = 'auth_login')
routerCuatro = routers.SimpleRouter()
routerCuatro.register('courses',CourseViewSet,basename = 'courses')
routerCinco = routers.SimpleRouter()
routerCinco.register('videos',VideoViewSet,basename = 'videos')
routerSeis = routers.SimpleRouter()
routerSeis.register('comments',CommentViewSet,basename = 'comments')
routerSiete = routers.SimpleRouter()
routerSiete.register('seem',SeemViewSet,basename = 'seems')
api = [
    path('',include(routerDos.urls)),
    path('',include(routerTres.urls)),
    path('',include(routerCuatro.urls)),
    path('',include(routerCinco.urls)),
    path('',include(routerSeis.urls)),
    path('',include(routerSeis.urls)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include(api))
]
