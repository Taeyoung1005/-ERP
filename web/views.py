from django.shortcuts import render, redirect
from api.models import *
from .forms import PostForm

def main(request):
    return render(request, 'web/main.html')
    

def coa_home(request, pk=None):
    return render(request, 'web/coa.html')

def coa_detail(request, pk):
    return render(request, 'web/coa_detail.html')

def coa_insert(request):
    return render(request, 'web/coa.html')

def coa_delete(request):
    return render(request, 'web/coa.html')


def product_home(request, pk=None):
    return render(request, 'web/product.html')

def product_detail(request, pk):
    return render(request, 'web/product_detail.html')

def product_insert(request):
    return render(request, 'web/product.html')

def product_delete(request):
    return render(request, 'web/product.html')


def hr_home(request, pk=None):
    return render(request, 'web/hr.html')

def hr_detail(request, pk):
    form = PostForm
    return render(request, 'web/hr_detail.html', {'form':form})

def hr_insert(request):
    return render(request, 'web/hr.html')

def hr_delete(request):
    return render(request, 'web/hr.html')


def login(request):
    return render(request, 'web/login.html')
