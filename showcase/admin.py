from django.contrib import admin
from django.db import models
from .models import Project, Project_section



# showcase/admin.py

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Project_section)
class Project_section_admin(admin.ModelAdmin):
    list_display = ("title", "project", "order")
    list_filter = ("project",)
    prepopulated_fields = {"slug": ("title",)}
