from django.urls import reverse
from django.db import models
from .validators import check_splcharacter


class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('show_gif', args = [self.id])


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[check_splcharacter])
    gifs = models.ManyToManyField(Gif)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_category', args = [self.id])


