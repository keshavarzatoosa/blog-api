from django.urls import path
from .views import BlogPostListView

app_name = 'api'

urlpatterns = [
    path('blog-posts/', BlogPostListView.as_view(), name='blog-post-list'),
]