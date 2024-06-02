from django.db import models
from django.conf import settings

class MovieList(models.Model):
    name = models.CharField(max_length=255)
    movies = models.JSONField(default=list)
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
