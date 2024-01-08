from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=28, unique=True)
    description = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=28)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField(default="Empty")
    value = models.IntegerField()

    def __str__(self):
        return f"{self.author} - {self.movie} - {self.value}"
