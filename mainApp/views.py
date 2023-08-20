from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from django.conf import settings


def home(Request):
    return render(Request, "index.html")


def contact(Request):
    if (Request.method == "POST"):
        c = Contact()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.subject = Request.POST.get("subject")
        c.message = Request.POST.get("message")
        c.save()
        messages.success("Thanks to contact us !!! I'm contact you soon.")
        subject = 'Thanks to contact us : Ravendra Singh'
        message = "Hello sir/madam "+c.name +"\nThank you to contact us\nI'm contact you soon\nRavendra Singh"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [c.email, ]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponseRedirect("#contact")

    return HttpResponseRedirect(Request, "#contact")


def about(Request):
    return render(Request, "index.html")


def skills(Request):
    return render(Request, "index.html")


def services(Request):
    return render(Request, "index.html")
