from django.db import models
from datetime import datetime
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

class Person (models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class ImageProfile (models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    image = models.URLField()

    def __str__(self):
        return f'ImageProfile of {self.person}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    released_date = models.DateField(default = datetime.now())
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='categories', blank=True)
# related_name is to retrieve the categories from a post

    def __str__(self):
        return f'Category {self.name}'
