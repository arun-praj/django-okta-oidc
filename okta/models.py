from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, db_index=True)
    email = models.EmailField(_('email address'), blank=True)
    REQUIRED_FIELDS = ['email', 'username']