from django.shortcuts import render

# Create your views here.


def index(request):
    titre= "profile"
    return render(request, 'index.html', {'titre': titre})

def contact(request):
    titre= "contact"
    return render(request, 'contact.html', {'titre': titre})

def newsletter(request):
    titre= "newsletter"
    return render(request, 'newsletter.html', {'titre': titre})

def dossiers(request):
    titre= "dossiers"
    return render(request, 'dossiers.html', {'titre': titre})