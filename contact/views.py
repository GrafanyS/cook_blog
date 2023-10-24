from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import ContactLink, About
from .forms import ContactForm


class ContactView(View):
    @staticmethod
    def get(request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    @staticmethod
    def get(request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {"about": about})
