from django.shortcuts import render, HttpResponseRedirect
from .models import Comments

# Create your views here.


def index(request):
    return render(request, 'land/index.html')


def posts(request):
    return render(request, 'land/posts.html')


def about(request):
    return render(request, 'land/about.html')


def services(request):
    return render(request, 'land/services.html')


def contacts(request):
    return render(request, 'land/contacts.html')


def info(request):
    return render(request, 'land/info.html')


def comments(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        report = request.POST.get('report')

        if email != "" and report != "":
            cmnt = Comments(email=email, report=report)
            cmnt.save()
        else:
            pass

        return HttpResponseRedirect("/")
    else:
        return render(request, 'land/index.html')
