from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact.as_view(), name="contact"),
    path("success/", views.success.as_view(), name="success"),

    # Project overview
    path("projects/<slug:project_slug>/", views.project_overview, name="project_overview"),

    # Individual section pages
    path(
        "projects/<slug:project_slug>/<slug:section_slug>/",
        views.section_detail,
        name="section_detail"
    ),
]
