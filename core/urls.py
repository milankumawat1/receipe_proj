"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from home.views import *
from vege.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home , name="home"),
    path('receipes/', receipes , name="receipes"),
    path('contact/',contact, name="contact"),
    path('about/', about , name="about"),
    path('success-page/', success_page, name="success_page"),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)