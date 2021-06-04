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
from django.conf.urls.static import static
from mysite import settings
from .views import CourseViewCreate, CourseViewList, CourseViewUpdate, CourseViewDelete, \
    LectureViewCreate, LectureViewList, LectureViewUpdate, LectureViewDelete, \
    HomeworkViewCreate, HomeworkViewReady, HomeworkViewList, SolutionViewCreate, SolutionViewList, \
    CommentViewCreate, RatingViewUpdate, CommentListView, \
    CourseAddUser, CourseDeleteStudent

app_name = 'mysite'
urlpatterns = [
    # work
    path('course/create/', CourseViewCreate.as_view()),
    path('course/', CourseViewList.as_view()),
    path('course/<int:course_id>/', CourseViewUpdate.as_view()),
    path('course/<int:course_id>/delete/', CourseViewDelete.as_view()),

    path('course/<int:course_id>/add-user/', CourseAddUser.as_view()),
    path('course/<int:course_id>/delete-student/', CourseDeleteStudent.as_view()),

    path('course/<int:course_id>/lecture/create/', LectureViewCreate.as_view()),
    path('course/<int:course_id>/lecture/', LectureViewList.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/', LectureViewUpdate.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/delete/', LectureViewDelete.as_view()),

    path('course/', CourseViewList.as_view()),
    path('course/<int:course_id>/lecture/', LectureViewList.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/create/', HomeworkViewCreate.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/', HomeworkViewList.as_view()),
    # Update rating
    path(
        'course/<int:course_id>/lecture/<int:lecture_id>/homework/<int:homework_id>/'
        'solution/<int:solution_id>/rating-update/', RatingViewUpdate.as_view()),

    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/<int:homework_id>/solution/create/',
         SolutionViewCreate.as_view()),
    # List solutions
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/solution/',
         SolutionViewList.as_view()),

    path(
        'course/<int:course_id>/lecture/<int:lecture_id>/homework/'
        '<int:homework_id>/solution/<int:solution_id>/comment/create/', CommentViewCreate.as_view()),
    path(
        'course/<int:course_id>/lecture/<int:lecture_id>/homework/'
        '<int:homework_id>/solution/<int:solution_id>/comment/', CommentListView.as_view()),
    path('course/<int:course_id>/lecture/<int:lecture_id>/homework/perfomed/', HomeworkViewReady.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
