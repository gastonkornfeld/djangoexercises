from django.db import models
from datetime import datetime

# Create your models here.


class Country(models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Film(models.Model):
    title= models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.now())
    created_in = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    available_in = models.ManyToManyField(Country)
    categories = models.ManyToManyField(Category, related_name='category')
    directors = models.ManyToManyField(Director)

    def __str__(self) -> str:
        return f'{self.title}'

