from django.shortcuts import render
from .models import Category, Gif
from .forms import CategoryForm


def create_category(request):

    if request.method == 'POST':
        form_filled = CategoryForm(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            Category.objects.create(name = name)

    # method - GET 
    context = {'form': CategoryForm}
    return render(request, 'create_category.html', context)