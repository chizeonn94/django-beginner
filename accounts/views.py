from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/dashboard.html')


def customer(request):
    return render(request, 'accounts/customer.html')


def products(request):
    return render(request, 'accounts/products.html')
