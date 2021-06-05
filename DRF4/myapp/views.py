from django.shortcuts import render
from .serializers import SerializerEmp
from .models import Employee
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .permiction import  Read_only
from rest_framework_jwt.authentication import JSONWebTokenAuthentication 
from .customauthentication import customAuth
# Create your views here.

class ListViewdata(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmp

class  EmployeeCRUD(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmp 
    authentication_classes=[customAuth,]
    permission_classes=[IsAuthenticated,]




