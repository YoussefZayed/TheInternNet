from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def index(request):
    contacts = Contact.objects.order_by('company')
    output = ",".join([c.first_Name + " " + c.last_Name for c in contacts])
    return HttpResponse(output)

def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)