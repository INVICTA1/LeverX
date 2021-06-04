from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Course(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    profile = models.ManyToManyField(User, related_name='courses', blank=True)


class Lecture(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    file = models.FileField(upload_to='documents/')
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE)


class Homework(models.Model):
    task = models.TextField()
    lecture = models.ForeignKey(Lecture, related_name='homework', on_delete=models.CASCADE)


class Solution(models.Model):
    solution = models.TextField()
    status = models.CharField(default='not_performed',
                              max_length=15,
                              choices=(('performed', 'Performed'), ('not_performed', 'Not performed')))
    rating = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)],
                                 null=True,
                                 default=None)
    homework = models.ForeignKey(Homework, related_name='homework', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='solutions', on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, related_name='comments', on_delete=models.CASCADE)
