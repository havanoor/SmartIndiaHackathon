"""SIH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings 
from django.conf.urls.static import static

from django.urls import  include,path

urlpatterns = [
    #urls of bank finance app
    path('Bank/',include("Bank.urls")),

    path('admin/', admin.site.urls),

    #urls of farmers portal  app
    path('',include('farmers.urls')),

    #urls of forward market app
    path('forward/',include('forward.urls')),
    path('weather/',include('weather.urls')),

    path('MlWork/', include('mlwork.urls')),
]
urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)