from .views import *
from django.urls import path


urlpatterns = [
    path('skills/', SkillsListCreateView.as_view()),
    path('skills-update-id/<int:pk>/', SkillsDetailView.as_view()),
    path('skills-view-id/<int:pk>/', skills_detail_view),
    path('skills-view-id/<int:pk>/', SkillsDetailAPIView.as_view()),
    path('skills-update-slug/<str:skills_slug>/', SkillsDetailUpdateSlugName.as_view()),
    path('skills-view-slug/<slug:skills_slug>/', skills_detail_view_slug),
    path('skills-view-slug/<str:skills_slug>/', SkillsDetailViewSlug.as_view()),
]
