import csv

from django.http import HttpResponse, HttpResponseRedirect
from api.resources import HrResource
from tablib import Dataset

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
        decoded_file = file.read().decode('euc-kr').splitlines()

        reader = csv.DictReader(decoded_file)
        for data in reader:
            근속일 = data['근속일']
            if 근속일 == '':
                근속일 = 0

            입사일 = data['입사일']
            if 입사일 == '':
                입사일 = None

            생년월일 = data['생년월일']
            if 생년월일 == '':
                생년월일 = None

            HR.objects.get_or_create(
                사번 = data['사번'],
                구분 = data['구분'],
                이름 = data['이름'],
                영문이름 = data['영문이름'],
                근무지 = data['근무지'],
                부서 = data['부서'],
                팀 = data['팀'],
                직급 = data['직급'],
                직책 = data['직책'],
                입사일 = 입사일,
                근속일 = 근속일,
                주민등록번호 = data['주민등록번호'],
                생년월일 = 생년월일,
                연락처 = data['연락처'],
                비상연락망 = data['비상연락망'],
                회사이메일 = data['회사이메일'],
                개인이메일 = data['개인이메일'],
                최종학력 = data['최종학력'],
                학위 = data['학위'],
                학교 = data['학교'],
                전공 = data['전공'],
                학점 = data['학점'],
                입사구분 = data['입사구분'],
                경력사항1 = data['경력사항1'],
                경력사항2 = data['경력사항2'],
                경력사항3 = data['경력사항3'],
                경력사항4 = data['경력사항4'],
                경력사항5 = data['경력사항5'],
                자격사항1 = data['자격사항1'],
                자격사항2 = data['자격사항2'],
                자격사항3 = data['자격사항3'],
                자격사항4 = data['자격사항4'],
                자격사항5 = data['자격사항5'],
                어학사항1 = data['어학사항1'],
                어학사항2 = data['어학사항2'],
                어학사항3 = data['어학사항3'],
                어학사항4 = data['어학사항4'],
                어학사항5 = data['어학사항5'],
            )
            return HttpResponseRedirect('/web/hr')

        # imported_data = dataset.load(new_hr.read().decode('euc-kr'), format='csv')
        # result = hr_resource.import_data(imported_data, dry_run=True, raise_errors=True)
        # print(imported_data)
        
        # if not result.has_errors():
        #     hr_resource.import_data(imported_data, dry_run=False)
        #     print("success")

    return render(request, 'web/hr/import.html')