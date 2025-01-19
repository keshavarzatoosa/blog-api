from django.contrib import admin
from .models import Tag, BlogPost

admin.site.register(Tag)
admin.site.register(BlogPost)