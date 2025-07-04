from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="No description")
    is_completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
