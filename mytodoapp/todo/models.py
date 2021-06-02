from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
