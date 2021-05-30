from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Course(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    profile = models.ManyToManyField(User, related_name='courses', blank=True)

class Lecture(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    file = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE)


class Homework(models.Model):
    work = models.TextField()
    status = models.CharField(default='not_performed',
                              max_length=15,
                              choices=(('performed', 'Performed'), ('not_performed', 'Not performed')))
    evaluation = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)],
                                     null=True,
                                     default=None)
    lecture = models.ForeignKey(Lecture, related_name='homework', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
