from .views import *
from django.urls import path


urlpatterns = [
    path('portfolio-category/', PortfolioCategoryView.as_view()),
    path('portfolio-category/<str:portfolio_category>/<int:pk>/', CategoryIdPortfolioAPIView.as_view()),
    path('portfolio-category/<str:portfolio_slug>/', PortfoliosByCategoryAPIView.as_view()),
    path('portfolio-data/', PortfolioView.as_view()),
    path('portfolio-data/<int:pk>/', PortfolioFilterById.as_view()),
    path('portfolio-data/<slug:portfolio_slug>/', PortfolioSlugView.as_view()),
]

