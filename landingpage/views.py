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


def contact(request):
    if request.method=="POST":
        # contact=Contact()
        message_name=request.POST.get['message-name']
        message_email=request.POST.get['message-email']
        message_subject=request.POST.get['message-subject']
        message=request.POST.get['message']

        # send an email
        # send_mail(
        #     message_name, # subject
        #     message_email, # from Email
        #     message_subject, # subject
        #     message, # message
        #     ['johnyves79@gmail.com', 'nadaljeanyves79@gmail.com'], # to Email
        #     )

        # contact.name=name
        # contact.email=email
        # contact.subject=subject
        # contact.message=message
        # contact.save()
        return render(request,'home.html', {'message_name'})
    else:
        return render(request,'home.html', {})


