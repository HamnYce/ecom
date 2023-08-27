from typing import Iterable, Optional
from django.db import models
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model
from users.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False,
        primary_key=True
    )
    username = models.CharField(
        max_length=150, unique=True, db_index=True,
        validators=[UnicodeUsernameValidator],
        null=False
    )
    gender = models.BooleanField(default=False)
