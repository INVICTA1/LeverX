from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from courses.models import Course, Lecture, Homework, Comment, Solution
from .serializer import UserSerializer, \
    CourseSerializer, CourseAllSerializer, \
    HomeworkSerializer, SolutionSerializer, \
    LectureSerializer, LectureAllSerializer, \
    CommentSerializer, RatingSerializer, CommentListSerializer
from rest_framework import generics, status
from django.contrib.auth import get_user_model
from .permissions import IsStudentOrReadOnly, IsTeacherOrReadOnly

User = get_user_model()


# Add, delete user
class CourseAddUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        profile_obj = User.objects.get(email=data['email'], profile=data['profile'])
        course = Course.objects.get(id=self.kwargs.get('course_id'))
        profile_obj.courses.add(course)
        course.profile.add(profile_obj)
        return Response(status=status.HTTP_201_CREATED)


class CourseDeleteStudent(generics.DestroyAPIView):
    queryset = User.objects.filter(profile='student')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        profile_obj = User.objects.get(email=data['email'], profile='student')
        course = Course.objects.get(id=self.kwargs.get('course_id'))
        profile_obj.courses.remove(course)
        return Response(status=status.HTTP_201_CREATED)


# Crud courses
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


class CourseViewUpdate(generics.UpdateAPIView):
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


# Crud lecture
class LectureViewCreate(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        file = request.FILES['file']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course.objects.get(id=self.kwargs.get('course_id'))
        lecture = Lecture.objects.create(name=data['name'], file=file, course=course)
        if course and lecture:
            lecture.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LectureViewList(generics.ListAPIView):
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly | IsStudentOrReadOnly)

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        user = User.objects.get(id=self.request.user.id, profile=self.request.user.profile)
        if Course.objects.filter(id=course_id, profile=user):
            return Lecture.objects.filter(course=course_id)


class LectureViewUpdate(generics.UpdateAPIView):
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


class HomeworkViewCreate(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lecture = Lecture.objects.get(id=self.kwargs.get('lecture_id'))
        homework = Homework.objects.create(task=data['task'], lecture=lecture)
        if homework and lecture:
            homework.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SolutionViewCreate(generics.CreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly | IsStudentOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(id=self.request.user.id, profile=self.request.user.profile)
        homework = Homework.objects.get(id=self.kwargs.get('homework_id'))
        solution = Solution.objects.create(solution=data['solution'],
                                           status=data['status'],
                                           homework=homework,
                                           user=user)

        solution.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HomeworkViewList(generics.ListAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly | IsStudentOrReadOnly)

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        lecture_id = self.kwargs.get('lecture_id')
        user = User.objects.get(id=self.request.user.id, profile=self.request.user.profile)
        if Course.objects.filter(id=course_id, lectures=lecture_id, profile=user).exists():
            return Homework.objects.filter(lecture=lecture_id)


class HomeworkViewReady(generics.ListAPIView):
    serializer_class = SolutionSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly | IsStudentOrReadOnly)

    def get_queryset(self):
        return Solution.objects.filter(status='performed')


class SolutionViewList(generics.ListAPIView):
    serializer_class = SolutionSerializer
    permission_classes = (IsAuthenticated, IsStudentOrReadOnly)

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id, profile=self.request.user.profile)
        return Solution.objects.filter(user=user)


class RatingViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Homework.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(id=self.kwargs.get('homework_id'))
        self.check_object_permissions(self.request, obj)
        return obj


class CommentViewCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly | IsStudentOrReadOnly)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = User.objects.get(id=request.user.id, courses=self.kwargs.get('course_id'))
        solution = Solution.objects.get(id=self.kwargs.get('homework_id'))
        new_comment = Comment.objects.create(comment=data['comment'],
                                             user=user_obj,
                                             solution=solution)
        new_comment.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrReadOnly | IsStudentOrReadOnly)

    def get_queryset(self):
        return Comment.objects.filter(solution=self.kwargs.get('solution_id'))
