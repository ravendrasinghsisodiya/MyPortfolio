from django.contrib import admin
from django.urls import path
from mainApp import views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.home),
    path("about/",mainapp.about),
    path("skill/",mainapp.skills),
    path("service/",mainapp.services),
    path("contact/",mainapp.contact),
]
