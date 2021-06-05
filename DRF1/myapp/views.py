from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
import io
from .models import Employee
from rest_framework import serializers
from .serializer import EmployeeSerializers
from rest_framework.renderers  import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class CreateDRF(View):
    def get(self,request,*args, **kwargs):
       json_data=request.body
       stream=io.BytesIO(json_data)
       data=JSONParser().parse(stream)
       id=data.get('id',None)
       if id is not None:
           emp=Employee.objects.get(id=id)
           serializer=EmployeeSerializers(emp)
           json_data=JSONRenderer().render(serializer.data)
           return HttpResponse(json_data,content_type='application/json')   
       data=Employee.objects.all()
       serializer=EmployeeSerializers(data,many=True)
       json_data=JSONRenderer().render(serializer.data)
       return HttpResponse(json_data,content_type='application/json')
    
     # create resource using post method
    def post(self,request,*args, **kwargs):
        data=request.body 
        stream=io.BytesIO(data)
        data=JSONParser().parse(stream)
        serializer=EmployeeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            json_data={'msg':'resource create sucessfully'}
            json_data=JSONRenderer().render(json_data)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    # put request for update
    def put(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializers(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data={'msg':'Update successfuly'}
            json_data=JSONRenderer().render(json_data)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


