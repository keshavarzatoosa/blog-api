from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    CHOICE_CATEGORY = [
        ('T', 'Technology'),
        ('S', 'Sport'),
        ('N', 'News')
    ]

    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.CharField(choices=CHOICE_CATEGORY, max_length=1)
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
