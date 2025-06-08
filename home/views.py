from django.shortcuts import render
from store.models import Product
# Create your views here.


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
      'products':products
    }
    return render(request,'index.html',context)

def login(request):
    return render(request,'auth/login.html')

def register(request):
    return render(request,'auth/register.html')