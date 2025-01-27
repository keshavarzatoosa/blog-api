from django.contrib import admin
from .models import Tag, BlogPost, Category

admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(Category)