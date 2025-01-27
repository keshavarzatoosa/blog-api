from rest_framework import serializers
from blog.models import BlogPost, Category


class BlogPostSerializer(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Category.objects.all(), required=False, help_text="Name of categories")
    tags = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True, required=False)

    class Meta:
        model = BlogPost
        fields = "__all__"