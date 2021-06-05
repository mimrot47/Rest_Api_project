from django.shortcuts import render
import requests

# Create your views here.
def gio_spa(request):
    ipaddr=request.META.get('HTTP_X_FORWARDED_FOR',"")or request.META.get('REMOTE_ADDR')
    ip ='http://api.ipstack.com/117.233.87.169?access_key=7181888fc4d7df2bb9004ce212d9c58a'
    # ip ='http://api.ipstack.com/'+str(ipaddr)+'?access_key=7181888fc4d7df2bb9004ce212d9c58a'  
    response=requests.get(ip)
    data=response.json()
    print(data)
    return render(request,'myapp/index.html',data)