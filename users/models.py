from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import EmailValidator

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        null=False, unique=True, db_index=True, validators=[EmailValidator], )
    has_profile = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def register_profile(self):
        self.has_profile = True
        self.save()
