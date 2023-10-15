from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContactList.as_view()),
    path('contact-class/<int:pk>/', ContactFilterById.as_view()),
    path('contact-func/<int:pk>/', contact_filter_by_id),
    path('contact-class/<str:contact_slug>/', ContactSlugView.as_view()),
    path('contact-func/<str:contact_slug>/', contact_slug_view),
]
