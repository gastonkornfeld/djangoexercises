from django.shortcuts import render, redirect

from django.http import HttpResponse
from . forms import HelpTextContactForm, AddBookForm

from .models import Book
# Create your views here.


def index(request):
    form = HelpTextContactForm()

    if request.method == 'POST':
        form_filled = HelpTextContactForm(request.POST)

        if form_filled.is_valid():
            subject =  form_filled.cleaned_data['subject']
            message = form_filled.cleaned_data['message']
            sender = form_filled.cleaned_data['sender']
            cc_myself = form_filled.cleaned_data['cc_myself']
            return render(request, 'index.html', {'subject': subject, 'message': message, 'sender':sender, 'cc_myself':cc_myself})
    return render(request, 'index.html', {'form': form})


def book_by_id(request, book_id):
   
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

def all_books(request):

    if request.method == 'POST':
        form_filled = AddBookForm(request.POST)
        print(form_filled)

        if form_filled.is_valid():
            title =  form_filled.cleaned_data['title']
            date =  form_filled.cleaned_data['date']
            joe = Book.objects.create(title = title, title2 = title, pub_date = date)
            books = Book.objects.all()
            return render(request, 'book_details.html', {'books':books, 'title':title})

    form = AddBookForm()
    books = Book.objects.all()
    return render(request, 'allbooks.html', {'books':books, 'form': form})

def deleteBook(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    form = AddBookForm()
    books = Book.objects.all()
    return redirect('all_books')

def about(request):
    return render(request, 'about.html', {})


