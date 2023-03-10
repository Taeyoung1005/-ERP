import csv

from django.http import HttpResponse, HttpResponseRedirect
from api.resources import HrResource
import psycopg2
from sqlalchemy import create_engine 
from django.core.files.storage import FileSystemStorage
import pandas as pd

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
def hr_retired(request, pk=None):
    return render(request, 'web/hr/hr_retired.html')

# 휴가자
def hr_leaveOfAbsense(request):
    return render(request, 'web/hr/hr_leaveOfAbsense')

def login(request):
    return render(request, 'web/login.html')

def hr_export(request):
    hr_resource = HrResource()
    dataset = hr_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv', charset="euc-kr")
    response['Content-Disposition'] = 'attachment; filename="hr.csv"'
    return response

def hr_import(request):
    if request.method == 'POST':
        file = request.FILES['importData']
        fs = FileSystemStorage().save(f"web\import_csv\{file}", file)
        pd_data = pd.read_csv(f"web\import_csv\{file}", encoding="euc-kr")
        conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="203.252.230.245", port="5432")
        engine = create_engine('postgresql://postgres:1234@203.252.230.245/postgres')
        pd_data.to_sql('api_hr', engine, if_exists='append', index=False)
        conn.close()
        return HttpResponseRedirect('/web/hr')
    return render(request, 'web/hr/import.html')

def test(request):
    return render(request, 'web/hr/test.html')