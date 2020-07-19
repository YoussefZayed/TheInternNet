from django.shortcuts import render
from .jobScrape import ScrapeLinkdin
# Create your views here.


def jobs4you(request):
    linkdinInfo = ScrapeLinkdin(request.GET['search'])
    linkdinInfo.scrapeSite()
    return render (request,'jobportal/Jobs4You.html',{"postList":linkdinInfo.jobPosting})
