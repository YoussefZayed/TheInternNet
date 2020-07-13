from django.shortcuts import render
from django.views import View

from .forms import URLForm

from bs4 import BeautifulSoup
import requests

# Create your views here.
class Base(View):
    def get(self, request, *awgs, **kwargs):
        return render(request, 'base.html')

class WebPortal(View):
    def get(self, request, *awgs, **kwargs):
        context = {}
        context['url_form'] = URLForm()
        return render(request, 'jobportal/form.html', context)

    def post(self, request):
        submitbutton= request.POST.get('Submit')

        name = ''
        weblink = ''

        form = URLForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            weblink = form.cleaned_data.get('weblink')

        context= {'url_form': URLForm(), 'name': name, 'weblink': weblink,
              'submitbutton': submitbutton}
        
        return render(request, 'jobportal/form.html', context)
