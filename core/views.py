from django.shortcuts import render
from .models import Project, Partner


def index(request):
    projects = Project.objects.all().order_by('-id')[:5]
    partners = Partner.objects.all()

    ctx = {
        'projects': projects,
        'partners': partners,
           }

    return render(request, 'index.html', ctx)


def about(request):
    ctx = {
        'partners': Partner.objects.all(),
    }
    return render(request, 'about.html', ctx)


def works(request):
    projects = Project.objects.all().order_by('-id')

    ctx = {
        'projects': projects,
    }
    return render(request, 'works.html', ctx)


def contact(request):
    return render(request, 'contact.html')


def work(request, slug):
    project = Project.objects.get(slug=slug)
    ctx = {
        'project': project,
    }

    return render(request, 'work.html', ctx)
