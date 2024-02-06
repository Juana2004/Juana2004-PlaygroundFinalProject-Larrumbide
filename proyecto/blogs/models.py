from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    author_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.body} {self.created_at} "
