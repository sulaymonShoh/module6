from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=28, unique=True)
    description = models.TextField(blank=False, null=False)


class Movie(models.Model):
    name = models.CharField(max_length=28)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
