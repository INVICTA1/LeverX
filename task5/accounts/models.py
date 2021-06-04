from django.db import models
from django.core import validators
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from rest_framework.permissions import IsAuthenticated


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    profile = models.CharField(choices=(('teacher', 'Teacher'), ('student', 'Student')), max_length=10)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = UserManager()