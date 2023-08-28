from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from profiles.models import UserProfile

# class CategoryStatus(models.Model):
#     name = models.CharField(max_length=10)


# NOTE: a decision to keep the name not a primary key has been made to speed up
#   results, one way to remedy this when presenting to the users in the front-end
#   could be to store the list of categories locally on the users device (with sqlite for example)
#   and hit the local database instead for quick searches
class Category(models.Model):
    # NOTE: these wil be defined inhouse
    name = models.CharField(max_length=100)


class Product(models.Model):
    owner = models.ForeignKey(UserProfile, to_field='username',
                              on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
