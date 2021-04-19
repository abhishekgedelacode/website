from django.shortcuts import render, HttpResponseRedirect
from .models import Holder


# Create your views here.


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        try:
            a = Holder.objects.get(email=email).password

            if pwd == a:
                return HttpResponseRedirect("/")
            else:
                return render(request, 'holder/signin.html')
        except:
            return render(request, 'holder/signin.html')
    else:
        return render(request, 'holder/signin.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')

        if email != "" and pwd != "" and cpwd != "" and pwd == cpwd:
            hdr = Holder(email=email, password=pwd)
            hdr.save()
        else:
            return render(request, 'holder/signup.html')
        return HttpResponseRedirect("/")
    else:
        return render(request, 'holder/signup.html')
