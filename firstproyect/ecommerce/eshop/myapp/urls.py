from django.urls import path



from . import views

# path function path(route, view, optional name)

urlpatterns = [
    path('', views.index, name= 'index'),
    path('book/<int:book_id>', views.book_by_id, name = 'book_by_id'),
    path('books', views.all_books, name = 'all_books'),
    path('about', views.about, name = 'about'),
    path('delete/<int:id>', views.deleteBook, name='delete_book')

]