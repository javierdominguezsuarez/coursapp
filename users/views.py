
from django.http import request, response
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import CustomUserSerializer, LoginSerializer, RegisterSerializer
from django.contrib.auth.models import Permission
from users.models import CustomUser
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
def login_view(request, *args, **kwargs):
    return render (request,"estilos/login.html")
def register_view(request, *args, **kwargs):
    return render (request,"estilos/signin.html")     
class RegisterViewSet (viewsets.ModelViewSet):
    serializer_class =  RegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    def create (self,request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user,token = serializer.save()
        data = {
                'user': CustomUserSerializer(user).data,
                'access_token': token,  
            }
        return Response(data, status=201)
class LoginViewSet (viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.filter(is_active = True)
    def create (self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user,token = serializer.save()
        data = {
            'user': CustomUserSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=201)