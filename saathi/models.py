from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(to=User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="pics", null=True, blank=True )
