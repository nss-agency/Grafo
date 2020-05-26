from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .decorators import check_recaptcha
from .models import Project, Partner


def send_contact(request):
    fname = request.POST.get('first_name', '')
    lname = request.POST.get('last_name', '')
    subject = 'Message from website'
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    whatsapp = request.POST.get('whatsapp', '')
    messages = 'Name and Surname: {} {} \nWhatsApp: {}\nFrom: {}\nMessage: \n{}\n\n\n\nSent From dark-render.com'.format(
        fname, lname, whatsapp, from_email, message)
    send_mail(subject, messages, 'noreply@createanimation.co', ['miheden428@whowlft.com'], fail_silently=False)


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


@check_recaptcha
def contact(request):
    ctx = {'success': False,
           'fail': False}
    if request.method == 'POST':
        if request.recaptcha_is_valid:
            send_contact(request)
            ctx['success'] = True
        else:
            ctx['fail'] = True
    return render(request, 'contact.html', ctx)


def work(request, slug):
    project = Project.objects.get(slug=slug)
    ctx = {
        'project': project,
    }

    return render(request, 'work.html', ctx)
