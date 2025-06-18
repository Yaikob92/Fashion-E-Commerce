from django.shortcuts import render,redirect
from . forms import RegistrationForm
from . models import Account
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
            user.save()
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request,'auth/register.html',context)

def login(request):
    return render(request,"auth/login.html")

def logout(request):
    pass
