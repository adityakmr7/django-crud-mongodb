from django.db import models
from slugger import AutoSlugField
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    overview = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title


        