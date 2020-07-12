from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
import re
from .models import EmailSent, Template



notLoggedInLink = '/login/'



def index(request):
    if request.user.is_authenticated:
        emails = Template.objects.filter(owner=request.user).order_by('name')
        template = loader.get_template('emails.html')
        context = {
            'email_List': emails,
            'usr': request.user,
        }
        return render( request,'emails.html', context)
    else:
        return redirect(notLoggedInLink)


def viewEmailTemp(request, email_id):
    if request.user.is_authenticated:
        email = get_object_or_404(Template,pk=email_id,owner=request.user)
        sent_list = EmailSent.objects.filter(template= email)

        return render(request, 'viewmail.html', {'email_list': sent_list,'email': email})
    else:
        return redirect(notLoggedInLink)

def viewCreatedEmail(request,email_id,sent_id):
    email = get_object_or_404(Template,pk=email_id,owner = request.user)
    sent = get_object_or_404(EmailSent,pk=sent_id,template=email)
    return render(request, 'usedtemp.html', {'res':sent ,'usedTemp': email})


# creates the email from template and filled in info provided in usetemp
def usedtemp(request, email_id):
    email = get_object_or_404(Template,pk=email_id,owner = request.user)
    content = email.content
    name = ""
    for field in request.POST:
        if field == "EmailUsedName":
            name = request.POST[field]
        content = content.replace(field,request.POST[field])
    sent = EmailSent(content = content,name=name, template = email)
    sent.save()
    return redirect('/emailing/viewCreatedEmail/'+str(email_id)+"/"+str(sent.id)+"/")

# uses a template, asks user for fields to fill in 
def usetemp(request, email_id):
    email = get_object_or_404(Template,pk=email_id)
    variables = re.findall(r'\$+\b[^\d\W]+',email.content)
    return render(request, 'useTemplate.html', {'email': email, 'variables': variables})

def createTemp(request):
    if request.user.is_authenticated:
        if request.POST:
            template = Template(name= request.POST['templateName'],content = request.POST['templateContent'],owner= request.user)
            template.save()
            return redirect('/emailing/')
        else:
            return render(request, 'createTemplate.html')
    else:
        return redirect(notLoggedInLink)

def editTemp(request, email_id):
    if request.user.is_authenticated:
        email = get_object_or_404(Template,pk=email_id,owner= request.user)
        if request.POST:
            email.name = request.POST['templateName']
            email.content = request.POST['templateContent']
            email.save()
            return redirect('/emailing/')
        else:
            return render(request, 'editTemplate.html', {'template': email})
    else:
        return redirect(notLoggedInLink)

def deleteTemp(request,email_id):
    email = get_object_or_404(Template,pk=email_id, owner =  request.user)
    email.delete()
    return redirect('/emailing/')