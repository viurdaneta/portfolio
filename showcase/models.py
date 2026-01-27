from django.db import models
from django.utils.text import slugify


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    content = models.TextField()
    tools = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    github = models.URLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project_section(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="sections",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    order = models.PositiveIntegerField(default=0)
    description = models.TextField()
    content = models.TextField()
    class Meta:
        ordering = ["order"]
        unique_together = ("project", "slug")
    def __str__(self):
        return f"{self.project.title} – {self.title}"