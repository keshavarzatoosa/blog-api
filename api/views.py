from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from blog.models import BlogPost, Category
from .serializers import BlogPostSerializer


class BlogPostListView(APIView):

    @swagger_auto_schema(
            operation_description="Get a list of all blog posts",
            responses={200: BlogPostSerializer(many=True)}
            )
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
            operation_description="Create a new blog post",
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'tags': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="tags",
                        example="['Tech', 'Sport']"
                    ),
                    'categories': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="Enter name of categories",
                        example="['Technology', 'Sport', 'Biology']"
                    ),
                    'title': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Title of blog post",
                        example="This is title"
                    ),
                    'content': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Content of blog post",
                        example="This is Content"
                    ),
                },
                required=['title', 'content']
            ),
            responses={
                201: BlogPostSerializer(),
                400: "Bad request"
                },
                )
    def post(self, request):
        data = request.data
        categories = data.pop('categories', [])
        category_instances = []
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            category_instances.append(category)
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            blog_post = serializer.save()
            blog_post.categories.set(category_instances)
            blog_post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetailView(APIView):

    @swagger_auto_schema(
            operation_description="Get a specific blog post by ID",
            responses={
                200: BlogPostSerializer(),
                404: "Not found"
                },
            manual_parameters=[
                openapi.Parameter(
                    name='id',
                    in_=openapi.IN_PATH,
                    description="ID of the blog post",
                    type=openapi.TYPE_INTEGER
                )
            ]
                )
    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def delete(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostUpdateView(APIView):

    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        data=request.data
        categories = data.pop('categories', [])
        category_instances = []
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            category_instances.append(category)
        serializer = BlogPostSerializer(blog_post, data=data, partial=False)
        if serializer.is_valid():
            updated_blog_post = serializer.save()
            updated_blog_post.categories.set(category_instances)
            updated_blog_post.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostSearchView(APIView):

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('term', '')
        if search_term:
            query = Q(title__icontains=search_term) | Q(content__icontains=search_term) | Q(category__icontains=search_term)
            posts = BlogPost.objects.filter(query)
        else:
            posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
