from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    tools = models.CharField(max_length=200)
    url = models.URLField()
    def __str__(self):
        return self.title