from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def works(request):
    return render(request, 'works.html')


def contact(request):
    return render(request, 'contact.html')
