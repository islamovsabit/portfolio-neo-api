from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register(r'messages-created', MessageViewSet, basename="messages")
# router.register(r'message-view', MessageView, basename="message-view")

urlpatterns = [
    # path("", include(router.urls)),
    path('message-created/', MessageViewSet.as_view()),
    path('message-view/', MessageView.as_view())
]
