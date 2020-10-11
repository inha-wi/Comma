"""comma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
import likelion.views
import notice.views
import program.views
import supporter.views
import introduce.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', likelion.views.main, name="main"),
    path('program/', notice.views.program, name="program"),
    path('notice_page/', notice.views.notice_page, name="notice_page"),   
    path('inquiry/', notice.views.inquiry, name="inquiry"),
    path('supporters/', notice.views.supporters, name="supporters"),
    path('supporter_page/', supporter.views.supporter_page, name="supporter_page"),
    path('class_page/', program.views.class_page, name="class_page"),
    path('program_form/', program.views.program_form, name="program_form"),
    path('supporters_form/', supporter.views.supporters_form, name="supporters_form"),
    path('index/', introduce.views.index, name="index"),
    path('vision/', introduce.views.vision, name='vision'),
    path('class_detail/', program.views.class_detail, name="class_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)