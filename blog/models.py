from django.db import models
from accounts.models import CustomUser 

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/blog')  
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title