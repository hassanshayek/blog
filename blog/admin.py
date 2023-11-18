from django.contrib import admin
from .models import Blog, BlogCategory
# Register your models here.

# admin.site.register(Blog)

@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date')
    # list_display = ('title', 'author',  'date')
    
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)    