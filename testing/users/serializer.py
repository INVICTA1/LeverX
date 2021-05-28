from rest_framework import serializers
from .models import Course
from django.contrib.auth import get_user_model

User = get_user_model()




class TeacherSerializer(serializers.ModelSerializer):
    # profile = serializers.CharField(default='teacher', max_length=10)

    class Meta:
        model = User
        fields = ('__all__')

    # def create(self, validated_data):
    #     user = User(email=validated_data['email'], username=validated_data['username'], profile='teacher')
    #     user.save()
    #     return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name','file')

class CourseAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')