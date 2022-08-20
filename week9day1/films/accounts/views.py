from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.


def sign_up_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        print('post')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'registration/sign_up.html', {'form': form})

    else:
        print('not')
        
        return render(request, 'registration/sign_up.html', {'form': form})

def login_user(request):
    form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def logout_user(request):
    form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def profile_user(request):
    
    return render(request, 'registration/profile.html', {})



    