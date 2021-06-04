from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Course, Lecture, Homework, Comment, Solution
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')


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

    class Meta:
        model = Homework
        fields = ('id', 'task', 'lecture')


class SolutionSerializer(serializers.ModelSerializer):
    homework = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Solution
        fields = ('id', 'solution', 'status', 'rating', 'homework', 'user')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'rating')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    solution = SolutionSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user', 'solution')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Comment
        fields = ('id', 'comment')
