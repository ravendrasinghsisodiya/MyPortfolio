from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import *


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
        messages.success(
            Request, "Thanks To Share Your Query With Us!!! I'm Contact You Soon")
    return HttpResponseRedirect(Request,"/contact/")


def about(Request):
    return render(Request,"index.html")


def skills(Request):
    return render(Request,"index.html")


def services(Request):
    return render(Request,"index.html")
