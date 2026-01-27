from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse, render, get_object_or_404
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormView
from django.urls import reverse
from .forms import ContactForm

from . import models


# Create your views here.
def index(request):
    return render(request, 'showcase/index.html')
def projects(request):
    projects = models.Project.objects.all()
    return render(request, 'showcase/projects.html', {'projects': projects})

class success(TemplateView):
    template_name = "showcase/success.html"


def project_overview(request, project_slug):
    project = get_object_or_404(models.Project, slug=project_slug)
    sections = project.sections.all()

    return render(request, "showcase/project_overview.html", {
        "project": project,
        "sections": sections,
    })


def project_detail(request, project_slug):
    project = get_object_or_404(models.Project, slug=project_slug)
    sections = models.project.sections.all()
    return render(request, 'showcase/project_detail.html', {
        'project': project,
        'sections': sections,
    })

def section_detail(request, project_slug, section_slug):
    section = get_object_or_404(
        models.Project_section,
        slug=section_slug,
        project__slug=project_slug
    )

    project = section.project

    next_section = (
        models.Project_section.objects
        .filter(project=project, order__gt=section.order)
        .order_by("order")
        .first()
    )

    prev_section = (
        models.Project_section.objects
        .filter(project=project, order__lt=section.order)
        .order_by("-order")
        .first()
    )

    return render(request, "showcase/section_detail.html", {
        "project": project,
        "section": section,
        "next_section": next_section,
        "prev_section": prev_section,
    })



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

        full_message = f"""
        You received a new message from {name} ({email}):

        Subject: {subject}

        {message}
        """

        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
            fail_silently=False,
        )

        return super().form_valid(form)
