"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path, include
from .views import CourseListView, TeacherListView, CourseCreateView

app_name = 'testing'
urlpatterns = [
    re_path('^course/$', CourseListView.as_view()),
    re_path('^course/create/$', CourseCreateView.as_view()),

    re_path('^teachers/$', TeacherListView.as_view()),

]
