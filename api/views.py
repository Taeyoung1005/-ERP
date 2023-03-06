from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from rest_framework_csv import renderers

from django_filters.rest_framework import DjangoFilterBackend

from .models import coa, product, User, HR
from .serializers import coaSerializer, productSerializer, UserSerializer, adminSerializer, HRSerializer

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

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