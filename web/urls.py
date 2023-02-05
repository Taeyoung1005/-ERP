from django.urls import path
from . import views

urlpatterns = [
    path('coa_insert/', views.coa_insert),
    path('coa_delete/', views.coa_delete),
    path('coa_detail/<int:pk>/', views.coa_detail),
    path('coa/<int:pk>/', views.coa_home),
    path('coa/', views.coa_home),

    path('product_insert/', views.product_insert),
    path('product_delete/', views.product_delete),
    path('coa_detail/<int:pk>/', views.coa_detail),
    path('coa/<int:pk>/', views.coa_home),
    path('product/', views.product_home),
    path('', views.main),

    path('login/', views.login)
]
