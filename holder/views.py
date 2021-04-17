from django.shortcuts import render

# Create your views here.


def signin(request):
    return render(request, 'holder/signin.html')


def signup(request):
    return render(request, 'holder/signup.html')
