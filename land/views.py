from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'land/index.html')


def about(request):
    return render(request, 'land/about.html')


def services(request):
    return render(request, 'land/services.html')


def contacts(request):
    return render(request, 'land/contacts.html')
