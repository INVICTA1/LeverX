from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")
#
#     class Meta:
#         permissions = [("teacher_permissions", 'permission for teacher')]
#
#     def __str__(self):
#         return self.user.username
#
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
#
#     class Meta:
#         permissions = [("student_permissions", 'permission for student')]
#
#     def __str__(self):
#         return self.user.username


class Course(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    file = models.CharField(db_index=True, max_length=255)
    person = models.ManyToManyField(User,related_name='person')
