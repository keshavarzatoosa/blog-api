from rest_framework import serializers
from blog.models import BlogPost, Category


class BlogPostSerializer(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Category.objects.all(), required=False)

    class Meta:
        model = BlogPost
        fields = "__all__"