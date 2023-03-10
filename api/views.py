from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import coa, product, User, HR
from .serializers import coaSerializer, productSerializer, UserSerializer, adminSerializer, HRSerializer

from django.shortcuts import render

class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class coaViewSet(viewsets.ModelViewSet):
    queryset = coa.objects.all()
    serializer_class = coaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination

class hrViewSet(viewsets.ModelViewSet):
    queryset = HR.objects.all()
    serializer_class = HRSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = '__all__'
    oldering_fields = '__all__'
    ordering = ['사번']
    search_fields = ['사번', '구분', '이름', '영문이름', '근무지', '부서', '팀', '직급', '직책', '입사일', '근속일', '주민등록번호', '생년월일', '연락처', '비상연락망', '회사이메일', '개인이메일', '주소', '최종학력', '학위', '학교', '전공', '학점', '입사구분', '경력사항1', '경력사항2', '경력사항3', '경력사항4', '경력사항5', '자격사항1', '자격사항2', '자격사항3', '자격사항4', '자격사항5', '어학사항1', '어학사항2', '어학사항3', '어학사항4', '어학사항5']


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class adminCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = adminSerializer

# class csvRenderer(renderers.CSVRenderer):
#     media_type = 'text/csv'
#     format = 'csv'
#     charset = 'utf-8'

#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return data.encoding(self.charset)

def test(request):
    return render(request, 'C:/Users/mu070/Desktop/Markcian-ERP/web/templates/web/hr/test.html')