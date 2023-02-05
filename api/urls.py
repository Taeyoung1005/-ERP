from django.urls import path, include
from rest_framework import routers

from .views import coaViewSet, productViewSet, UserCreate, adminCreate

router = routers.SimpleRouter()
router.register(r'coa', coaViewSet)
router.register(r'product', productViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('signup/', UserCreate.as_view()),
    path('signup-admin/', adminCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]