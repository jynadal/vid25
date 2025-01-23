from django.shortcuts import render
from .models import Contact
# from .models import Subscriber
from django.http import HttpResponse


def home(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thanks for contact us.</h1>")

    

    return render(request, 'home.html', {})
