from typing import Iterable, Optional
from django.db import models
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model
from users.models import User

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(
        max_length=150, unique=True, db_index=True,
        validators=[UnicodeUsernameValidator], primary_key=True,
        null=False
    )
    email = models.OneToOneField(
        settings.AUTH_USER_MODEL, to_field='email', name='email', on_delete=models.DO_NOTHING, null=False
    )
    gender = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        user = get_user_model().objects.filter(email=self.email).first()
        user.has_profile = True
        user.save()
        super().save(*args, **kwargs)
