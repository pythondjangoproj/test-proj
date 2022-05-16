from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    IGL_Username = models.CharField(max_length=255, null=True, blank=True)
    is_varified = models.BooleanField(default=False)
    terms_and_condition_agreement = models.BooleanField(default=True)
    code_of_conduct_agreement = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
