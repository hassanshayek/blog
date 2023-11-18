from django.urls import path
from .views import home, post, create_blog
urlpatterns = [
    path("", home, name = 'home'),
    path("post/", post, name = 'post'),
    path('create_blog/', create_blog, name='create_blog'),
]