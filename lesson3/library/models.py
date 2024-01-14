# from django.contrib.auth.models import User
# from django.db import models
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=20, unique=True, blank=False, null=False)
#     slug = models.SlugField(unique=True, blank=False, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=70, blank=False, null=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#
# class BookRecord(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     day = models.DateField()
#
#     class Meta:
#         verbose_name = "Book Record"
#         verbose_name_plural = "Book Records"
