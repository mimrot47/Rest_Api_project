from django.shortcuts import render
from .serializer import SerializerEmp
from rest_framework.views import APIView
from .models import Employee
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.generics import DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView

# Create your views here.



class EmployeeAPIView(ListAPIView):
    # queryset=Employee.objects.all()
    serializer_class=SerializerEmp
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs
    




class EmployeeCreateView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmp


# class EmployeeAPIView(APIView):
#     def get(self,Request,format=None):
#         qs=Employee.objects.all()
#         serializer=SerializerEmp(qs,many=True)
#         return Response(serializer.data)

class RetriveData(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmp


class UpdateData(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmp
    lookup_field='id'


class DelateData(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class= SerializerEmp
    lookup_field='id'

class ListCreatData(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=SerializerEmp

# class RetriveUpdatedata(RetrieveUpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class= SerializerEmp
#     lookup_field='id'