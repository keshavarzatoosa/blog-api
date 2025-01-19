from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(APIView):

    def get(self, request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
