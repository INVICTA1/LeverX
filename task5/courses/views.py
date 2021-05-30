from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Course, Lecture, Homework, Comment
from .serializer import UserSerializer, \
    CourseSerializer, CourseAllSerializer, \
    HomeworkSerializer, HomeworkAllSerializer, \
    LectureSerializer, LectureAllSerializer, \
    EvaluationSerializer, CommentSerializer
from rest_framework import generics, status
from django.contrib.auth import get_user_model
from .permissions import IsStudentOrReadOnly, IsTeacherOrReadOnly

User = get_user_model()


# class CourseAddStudent(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = self.get_serializer(data=data)
#         serializer.profile = request.user
#         serializer.is_valid(raise_exception=True)
#         profile_obj = User.objects.get(email=data['email'])
#         new_course = Course.objects.get(id=self.kwargs.get('course_id'))
#         new_course.profile.add(email=data['email'])
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#

class CourseViewCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.profile = request.user
        serializer.is_valid(raise_exception=True)
        profile_obj = User.objects.get(id=request.user.id)
        new_course = Course.objects.create(name=data['name'])
        new_course.save()
        new_course.profile.add(profile_obj)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CourseViewList(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        profile = self.request.user.id
        return Course.objects.filter(profile=profile)


class CourseViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.kwargs.get('course_id'))
        self.check_object_permissions(self.request, obj)
        return obj


class CourseViewDelete(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.kwargs.get('course_id'))
        self.check_object_permissions(self.request, obj)
        return obj


class LectureViewCreate(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course.objects.get(id=self.kwargs.get('course_id'))
        lecture = Lecture.objects.create(name=data['name'], file=data['file'], course=course)
        if course and lecture:
            lecture.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LectureViewList(generics.ListAPIView):
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_queryset(self):
        course = self.kwargs.get('course_id')
        return Lecture.objects.filter(course=course)


class LectureViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.kwargs.get('lecture_id'))
        self.check_object_permissions(self.request, obj)
        return obj


class LectureViewDelete(generics.DestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.kwargs.get('lecture_id'))
        self.check_object_permissions(self.request, obj)
        return obj


# -------------------

class LectureAllView(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureAllSerializer
    permission_classes = (IsAuthenticated,)


# --------------

class HomeworkViewCreate(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lecture = Lecture.objects.get(id=self.kwargs.get('lecture_id'))
        homework = Homework.objects.create(work=data['work'], lecture=lecture)
        if homework and lecture:
            homework.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(status='performed')


class HomeworkViewList(generics.ListAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_queryset(self):
        lecture = self.kwargs.get('lecture_id')
        return Homework.objects.filter(lecture=lecture)


class HomeworkViewReady(generics.ListAPIView):
    serializer_class = HomeworkAllSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        lecture = self.kwargs.get('lecture_id')
        return Homework.objects.filter(lecture=lecture, status='performed')


class EvaluationViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Homework.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.kwargs.get('homework_id'))
        self.check_object_permissions(self.request, obj)
        return obj


class CommentViewCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.profile = request.user
        serializer.is_valid(raise_exception=True)
        user_obj = User.objects.get(id=request.user.id)
        homework_obj = Homework.objects.get(id=self.kwargs.get('homework_id'))
        new_comment = Comment.objects.create(comment=data['comment'],
                                             user=user_obj,
                                             homework=homework_obj)
        new_comment.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
