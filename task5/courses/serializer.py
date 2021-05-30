from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Course, Lecture, Homework, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CourseSerializer(serializers.ModelSerializer):
    profile = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'profile')


class CourseAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'profile', 'lectures')


class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ('id', 'name', 'file', 'course')


class LectureAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'name', 'file', 'course', 'homework')


class HomeworkSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(read_only=True)
    evaluation = serializers.IntegerField(read_only=True)

    class Meta:
        model = Homework
        fields = ('id', 'work', 'evaluation', 'lecture')


class HomeworkAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'work', 'status', 'evaluation', 'lecture')


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'evaluation')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    homework = HomeworkSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'homework', 'comment')
