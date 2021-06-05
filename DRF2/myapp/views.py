from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
from .serializers import Nameserializer
# Create your views here.
class myApiView(APIView):
    def get(self,request,*args, **kwargs):
        color=['RED ','BLUE','BLACK']
        return Response({'msg':'hi rk how are you','color':color})
    
    def post(self,request,*args, **kwargs):
        serializer=Nameserializer(data=request.data)
        if serializer.is_valid():
          name=serializer.data.get('name')
          msg='Hello {} Wish You Happy New Year !!!'.format(name)
          return Response({'msg':msg})
        return Response(serializer.errors,status=400)
    def delete(self,request,*args, **kwargs):
        return Response({'msg':'This massage from Delete  Request '})
    def patch(self,reqeust,*args, **kwargs):
        return Response({'msg':'This massage from patch request'})
    def put(self,reqeust,*args, **kwargs):
        return Response({'msg':'This massage from put request'})

from rest_framework.viewsets import ViewSet

class DemoViewste(ViewSet):
    def list(self,request):
        color=['red','blue']
        return Response({'msg':'This is demo'})
    def create(self,request):
        serializer=Nameserializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='hi {} this is demo '.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors)