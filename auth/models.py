from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .managers import UserManager
from .validators import phone_regex_validator


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_('Email'), max_length=150,
                              unique=True, db_index=True, null=False, blank=False)
    phone = models.CharField(verbose_name=_('Phone'), max_length=25,
                             unique=True, db_index=True, null=False, blank=False, validators=(phone_regex_validator,))

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone']
