from django.shortcuts import render

from contact.core.forms import ContactForm


def home(request):
    context = {'form': ContactForm()}
    return render(request, 'index.html', context)
