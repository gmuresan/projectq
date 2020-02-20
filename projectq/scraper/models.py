from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Page(models.Model):
    def __str__(self):
        return self.url

    url = models.URLField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    resynced_on = models.DateTimeField(null=True, blank=True)

class Image(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)
    date_taken = models.DateField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)

"""
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (),
                {
                   'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
"""

