from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {['Not completed', 'Completed'][self.completed]}"
