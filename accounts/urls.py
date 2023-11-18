from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login,register, author

urlpatterns = [
    path("profile/", author, name = 'author'),
    path('register/', register, name='register'),
    
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]