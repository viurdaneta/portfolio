from django.contrib import admin

# Register your models here.
from .models import Project, ProjectImage

admin.site.register(Project)
admin.site.register(ProjectImage)