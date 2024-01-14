from django.contrib import admin

from .models import Book, Category, BookRecord


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category",)
    search_fields = ("title", "author")
    list_filter = ("category",)


@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    pass
