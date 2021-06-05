from django.shortcuts import render
from .serializers import EmpSelizers
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class MView(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmpSelizers
    search_fields=('ename')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ename', 'eno']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['ename', 'eno']
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__icontains=name)
    #     return qs





class List_view(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSelizers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ename', 'eno']
    # search_fields=('ename')
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=qs.filter(ename__icontains=name)
    #     return qs
