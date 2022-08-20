

from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('add_film', views.add_film, name='add_film'),
    path('films', views.all_films, name='all_films'),
    path('add_director', views.add_director, name='add_director'),
    path('edit_director/<int:pk>', views.edit_director, name = 'edit_director'),
    path('edit_film/<int:pk>', views.edit_film, name = 'edit_film'),

]

