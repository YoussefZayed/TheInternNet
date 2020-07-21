from django.shortcuts import render
from .jobScrape import ScrapeLinkdin
# Create your views here.


def jobs4you(request):
    if len(request.GET)>0:
        linkdinInfo = ScrapeLinkdin(request.GET['search'])
    else:
        linkdinInfo = ScrapeLinkdin("Software Development")
    linkdinInfo.scrapeSite()
    return render (request,'jobportal/Jobs4You.html',{"postList":linkdinInfo.jobPosting})
