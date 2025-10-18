from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=title)
    time_update = models.DateTimeField(auto_now=True)
    is_pablished = models.BooleanField(default=True)