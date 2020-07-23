from django.shortcuts import render, redirect
from .jobScrape import ScrapeLinkdin
from django.contrib.auth.decorators import login_required
from .models import UserSaved
from django.template.defaulttags import register

# Create your views here.


def jobs4you(request):
    if len(request.GET)>0:
        linkdinInfo = ScrapeLinkdin(request.GET['search'])
    else:
        linkdinInfo = ScrapeLinkdin("Software Development")
    linkdinInfo.scrapeSite()
    return render (request,'jobportal/Jobs4You.html',{"postList":linkdinInfo.jobPosting})

def savePosts(request):
    if request.user.is_authenticated:
        if request.POST:
            print("post")
            owner = request.user
            company = request.POST['Company1']
            link = request.POST['Link1']
            title = request.POST['Title1']
            location = request.POST['Location1']

            user_saved = UserSaved(owner=owner,title=title,company=company,location=location,link=link)
            user_saved.save()
    if len(request.GET)>0:
        linkdinInfo = ScrapeLinkdin(request.GET['search'])
    else:
        linkdinInfo = ScrapeLinkdin("Software Development")
    linkdinInfo.scrapeSite()
    return render (request,'jobportal/Jobs4You.html',{"postList":linkdinInfo.jobPosting})


@login_required(login_url='login')
def savedJobs(request):
    all_saved = list(UserSaved.objects.all())
    temp = all_saved[:]

    count = -1
    for x in range(len(temp)):
        count+=1
        if all_saved[count].owner == request.user:
            continue
        else:
            all_saved.pop(count)
            count-=1
    lenSav = round(len(all_saved)/3)
    print(lenSav)
    return render (request,'jobportal/savedJobs.html',{"savedData":all_saved,"lengthSaved":lenSav})


@register.filter
def get_range(value):
    return range(value)
