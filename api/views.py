from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import coa, product, User
from .serializers import coaSerializer, productSerializer, UserSerializer, adminSerializer

class coaPagination(PageNumberPagination):
    page_size = 10

class coaViewSet(viewsets.ModelViewSet):
    queryset = coa.objects.all()
    serializer_class = coaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = coaPagination

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    permission_classes = [IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class adminCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = adminSerializer