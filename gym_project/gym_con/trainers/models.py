from datetime import date
from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    description = models.TextField(max_length=70)
    image = models.ImageField(upload_to="blogs/%Y/%m/%d/")
    date = models.DateTimeField(auto_now=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name