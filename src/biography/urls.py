from django.urls import path
from .views import *


urlpatterns = [
    path('biography/', BiographyView.as_view()),

    path('biography-update/<int:pk>/', BiographyDetailUpdateView.as_view()),
    path('biography-update/<slug:biography_slug>/', BiographyDetailUpdateSlugName.as_view()),

    path('biography-view-id-func/<int:pk>/', biography_objects_view_id),
    path('biography-view-id-class/<int:pk>/', BiographyIdView.as_view()),

    path('biography-view-slug-func/<slug:biography_slug>/', biography_view_slug_name),
    path('biography-view-slug-class/<slug:biography_slug>/', BiographySlugView.as_view()),
]
