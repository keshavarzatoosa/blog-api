from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    tags = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
