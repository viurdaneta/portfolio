from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact.as_view(), name="contact"),
    path("success/", views.success.as_view(), name="success"),
]