from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from blog.models import Blog 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import CustomUser


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('author')  
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'accounts/login.html', {'error_message': error_message})
    else:
        return render(request, 'accounts/login.html')

@login_required
def author(request):
    user = CustomUser
    author_articles = Blog.objects.filter(author=request.user)
    context = {
        'author_articles': author_articles
    }
    return render(request, 'accounts/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # save uploaded profile picture
            if request.FILES.get('profile_picture'):
                user = form.instance
                user.profile_picture = request.FILES['profile_picture']
                user.save()
            return redirect('login')  # Redirect to the login
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

