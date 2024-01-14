from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import FloatField


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male',),
        ('F', 'Female'),
    ]

    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)


class Publisher(AbstractBaseModel):
    name = models.CharField(max_length=86)
    is_active = models.BooleanField(default=False)


class Book(AbstractBaseModel):
    name = models.CharField(max_length=60)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = FloatField()
    authors = models.ManyToManyField(Author, related_name='books')
