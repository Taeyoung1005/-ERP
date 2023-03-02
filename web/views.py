from django.http import HttpResponse
from api.resources import HrResource

from django.shortcuts import render, redirect
from api.models import *
from .forms import PostForm

def main(request):
    return render(request, 'web/main.html')
    

def coa_home(request, pk=None):
    return render(request, 'web/coa/coa.html')

def coa_detail(request, pk):
    return render(request, 'web/coa/coa_detail.html')

def coa_insert(request):
    return render(request, 'web/coa/coa.html')

def coa_delete(request):
    return render(request, 'web/coa/coa.html')


def product_home(request, pk=None):
    return render(request, 'web/product/product.html')

def product_detail(request, pk):
    return render(request, 'web/product/product_detail.html')

def product_insert(request):
    return render(request, 'web/product/product.html')

def product_delete(request):
    return render(request, 'web/product/product.html')


# 재직자
def hr_home(request, pk=None):
    return render(request, 'web/hr/hr.html')

# 상세페이지
def hr_detail(request, pk):
    form = PostForm
    return render(request, 'web/hr/hr_detail.html', {'form':form})


# 삭제
def hr_delete(request):
    return render(request, 'web/hr/hr.html')

# 퇴직자
def hr_retired(request):
    return render(request, 'web/hr/hr_retired.html')

# 휴가자
def hr_leaveOfAbsense(request):
    return render(request, 'web/hr/hr_leaveOfAbsense')


def login(request):
    return render(request, 'web/login.html')

def hr_export(request):
    hr_resource = HrResource()
    print(hr_resource)
    dataset = hr_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv', charset="euc-kr")
    response['Content-Disposition'] = 'attachment; filename="hr.csv"'
    return response