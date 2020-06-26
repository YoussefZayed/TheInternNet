from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render (request,'Pages/register.html',context)

def login(request):
    context = {}
    return render (request,'Pages/login.html',context)
