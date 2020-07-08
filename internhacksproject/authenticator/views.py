from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/emailing/')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render (request,'Pages/register.html',context)

def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/emailing/')
    else:
        form = AuthenticationForm()

    context = {'form':form}
    return render (request,'Pages/logIn.html',context)

def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

@login_required(login_url='login')
def test(request):
    form = AuthenticationForm()
    context = {'form':form}
    return render (request,'Pages/test.html',context)
