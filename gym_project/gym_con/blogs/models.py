from datetime import date
from email.policy import default
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True )
    subtitle = models.CharField(max_length=200, unique=True )
    content = RichTextField()
    image = models.ImageField(upload_to="blogs/%Y/%m/%d/", default="blogs/default_blog_image.jpg")
    date = models.DateTimeField(auto_now=True)
    avaiable = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.title