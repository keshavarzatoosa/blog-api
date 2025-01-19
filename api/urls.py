from django.urls import path
from .views import BlogPostListView, BlogPostDetailView

app_name = 'api'

urlpatterns = [
    path('blog-posts/', BlogPostListView.as_view(), name='blog-post-list'),
    path('blog-post/<int:pk>', BlogPostDetailView.as_view(), name='blog-post-detail'),
]