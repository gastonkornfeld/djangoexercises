from unicodedata import category
from django.contrib import admin

# Register your models here.

from .models import Book, Person, ImageProfile, Category, Post
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(ImageProfile)
admin.site.register(Category)
admin.site.register(Post)

