"""DRF4 URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from myapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',views.EmployeeCRUD,basename='api')
from rest_framework.authtoken import views as v
from rest_framework_jwt.views import verify_jwt_token,obtain_jwt_token,refresh_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.ListViewdata.as_view()),
    path('',include(router.urls)),
    path('get-api-token/', v.obtain_auth_token,name='get-api-token'),
    #http POST http://127.0.0.1:8000/get-api-token/ username="gokul" password="Rk@312151"
    path('jwt-token-varify/',verify_jwt_token),
    path('jwt-token/',obtain_jwt_token),
    #http POST http://127.0.0.1:8000/jwt-token-obtain/ username="gokul" password="Rk@312151"
    path('jwt-token-refresh/',refresh_jwt_token)
]
