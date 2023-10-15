from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'certificates', CertificateViewSet)

urlpatterns = [
    path('certificate-class/', CertificateViewSet.as_view()),
    path('certificate-func/', certificate_view_set),
    path('certificate-class/<int:id>/', CertificateViewId.as_view()),
    path('certificate-func/<int:pk>/', certificate_view_id),
]
