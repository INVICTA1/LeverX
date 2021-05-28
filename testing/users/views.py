from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializer import CourseSerializer, TeacherSerializer, CourseAllSerializer
from rest_framework import generics, status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import viewsets


class TeacherListView(generics.ListAPIView):
    queryset = User.objects.filter(profile='teacher')
    # queryset = User.objects.all()
    serializer_class = TeacherSerializer


class TeacherCreateView(generics.ListAPIView):
    queryset = User.objects.filter(profile='teacher')
    # queryset = User.objects.all()
    serializer_class = TeacherSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseAllSerializer




class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        print('-----------------')
        print(request)
        print(request.user)
        print(request.session)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
# class UserList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticatedOrWriteOnly,)
#     serializer_class = UserSerializer
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class CourseCreateView(generics.CreateAPIView):
#     serializer_class = CourseSerializer


# class TeacherAPIView(generics.CreateAPIView):
#     queryset = AUTH_USER_MODEL.objects.all()
#     serializer_class = UserSerializer
# def post(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response(serializer.data,  headers=headers)


# class TeacherView(generics.ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def perform_create(self, serializer):
#         teacher = get_object_or_404(Teacher, id=self.request.data.get('pk'))
#         return serializer.save(teacher=teacher)
#
#
# class SingleTeacherView(generics.RetrieveUpdateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#
# class CourseViewList(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseViewUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseViewDelete(generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseViewCreate(generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseViewList(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseViewUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class CourseViewDelete(generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
