from django.shortcuts import render,redirect
from .models import Blog, BlogCategory
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.contrib import messages

def home(request):
    featured_blogs = Blog.objects.filter(is_featured=True)
    non_featured_blogs = Blog.objects.filter(is_featured=False)
    account_profile = CustomUser.objects.all()

    context = {
        'featured_blogs': featured_blogs,
        'non_featured_blogs': non_featured_blogs,
        'account_profile': account_profile
    }

    return render(request, "index.html", context)


def post(request):
    return render(request, "post.html")


# @login_required
# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             category_id = request.POST.get('category')
#             new_category_name = request.POST.get('new_category')

#             if category_id:
#                 category = BlogCategory.objects.get(pk=category_id)
#             elif new_category_name:
#                 category, created = BlogCategory.objects.get_or_create(name=new_category_name)

#             if category:
#                 blog = form.save(commit=False)
#                 blog.author = request.user
#                 blog.category = category
#                 blog.save()
#                 return redirect('home')  
#     else:
#         form = BlogForm()
#     categories = BlogCategory.objects.all()
#     return render(request, 'create_blog.html', {'form': form, 'categories': categories})




@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            category_id = request.POST.get('category')
            new_category_name = request.POST.get('new_category')

            if category_id:
                category = BlogCategory.objects.get(pk=category_id)
            elif new_category_name:
                category, created = BlogCategory.objects.get_or_create(name=new_category_name)

            if category:
                blog = form.save(commit=False)
                blog.author = request.user
                blog.category = category
                blog.save()
                messages.success(request, 'Blog post created successfully.')
                return redirect('home')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')

    else:
        form = BlogForm()
    categories = BlogCategory.objects.all()
    return render(request, 'create_blog.html', {'form': form, 'categories': categories})


