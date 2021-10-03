from django.shortcuts import render
from rest_framework import generics
from .models import RegisterModel
from .serializers import RegisterSerializer

# Create your views here.

class RegisterView(generics.ListCreateAPIView):
    queryset = RegisterModel.objects.all()
    serializer_class = RegisterSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegisterModel.objects.all()
    serializer_class = RegisterSerializer