from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView
from . import models

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'showcase/index.html')
def projects(request):
    projects = models.Project.objects.all()
    return render(request, 'showcase/projects.html', {'projects': projects})

class success(TemplateView):
    template_name = "showcase/success.html"
class contact(FormView):
    form_class = ContactForm
    template_name = "showcase/contact.html"

    def get_success_url(self):
        return reverse("success")
    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        full_message = f"""Received message below from {email}, {subject}________________________ {message}"""
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(contact, self).form_valid(form)
