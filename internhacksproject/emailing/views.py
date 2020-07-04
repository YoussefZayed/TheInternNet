from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
import re
from .models import Contact, Email

def index(request):
    emails = Email.objects.order_by('name')
    template = loader.get_template('emails.html')
    context = {
        'email_List': emails,
    }
    return HttpResponse(template.render(context, request))

def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)

def viewEmailTemp(request, email_id):
    email = get_object_or_404(Email,pk=email_id)
    return render(request, 'viewmail.html', {'email': email})


# creates the email from template and filled in info provided in usetemp
def usedtemp(request, email_id):
    email = get_object_or_404(Email,pk=email_id)
    content = email.content
    for field in request.POST:
        content = content.replace(field,request.POST[field])
    return render(request, 'usedtemp.html', {'res':content ,'usedTemp': email})

# uses a template, asks user for fields to fill in 
def usetemp(request, email_id):
    email = get_object_or_404(Email,pk=email_id)
    variables = re.findall(r'\$+\b[^\d\W]+',email.content)

    return render(request, 'useTemplate.html', {'email': email, 'variables': variables})

def createTemp(request):
    if request.POST:
        template = Email(name= request.POST['templateName'],content = request.POST['templateContent'])
        template.save()
        return redirect('/emailing/')
    else:
        return render(request, 'createTemplate.html')

def editTemp(request, email_id):
    email = get_object_or_404(Email,pk=email_id)
    if request.POST:
        email.name = request.POST['templateName']
        email.content = request.POST['templateContent']
        email.save()
        return redirect('/emailing/')
    else:
        return render(request, 'editTemplate.html', {'template': email})

def deleteTemp(request,email_id):
    email = get_object_or_404(Email,pk=email_id)
    email.delete()
    return redirect('/emailing/')