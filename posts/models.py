from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=280)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
