from django.shortcuts import render, redirect

from .models import Director, Film
# Create your views here.
from .forms import AddFilmForm, AddDirectorForm

def homepage(request):
    films = Film.objects.all()
    directors = Director.objects.all()
    return render(request, 'homepage.html', {'films': films, 'directors': directors})


def add_film(request):
    form = AddFilmForm()
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./homepage')

    return render(request, 'add_film.html', {'form': form})

def edit_film(request, pk):
    film = Film.objects.get(id = pk)
    form = AddFilmForm(instance = film)
    if request.method == 'POST':
        form = AddFilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'add_film.html', {'form': form})

    


def add_director(request):
    form = AddDirectorForm()
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./homepage')

    return render(request, 'add_director.html', {'form': form})

def edit_director(request, pk):
    director = Director.objects.get(id = pk)
    form = AddDirectorForm(instance = director)
    if request.method == 'POST':
        form = AddDirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'add_director.html', {'form': form})


def all_films(request):
    films = Film.objects.all()
    directors = Director.objects.all()
    return render(request, 'films.html', {'films': films, 'directors': directors})
