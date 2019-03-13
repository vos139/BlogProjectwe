from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import mark_safe
#from django.db.models.signals import post_save

class User(AbstractUser):
    is_learner = models.BooleanField(default=False)
    is_consultant = models.BooleanField(default=False)

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self);
