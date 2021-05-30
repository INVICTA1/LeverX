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
from django.urls import path, include, re_path
from .views import CourseViewCreate, CourseViewList, CourseViewUpdate, CourseViewDelete, \
    LectureViewCreate, LectureViewList, LectureViewUpdate, LectureViewDelete, LectureAllView, \
    HomeworkViewCreate, HomeworkViewReady, HomeworkViewList, \
    EvaluationViewUpdate, CommentViewCreate
    # CourseAddStudent, \

app_name = 'mysite'
urlpatterns = [
    # work
    path('course/create/', CourseViewCreate.as_view()),
    path('course/', CourseViewList.as_view()),
    path('course/<int:course_id>/', CourseViewUpdate.as_view()),
    path('course/<int:course_id>/delete/', CourseViewDelete.as_view()),
    # path('course/<int:course_id>/add_student/', CourseAddStudent.as_view()),

    path('course/<int:course_id>/lecture/create', LectureViewCreate.as_view()),
    path('course/<int:course_id>/lecture/', LectureViewList.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/', LectureViewUpdate.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/delete/', LectureViewDelete.as_view()),
    # path('course/lecture/all/', LectureAllView.as_view()),

    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/create/', HomeworkViewCreate.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/', HomeworkViewList.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/<int:homework_id>/evaluation/',EvaluationViewUpdate.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/perfomed/', HomeworkViewReady.as_view()),

    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/<int:homework_id>/comment/', CommentViewCreate.as_view()),

]
