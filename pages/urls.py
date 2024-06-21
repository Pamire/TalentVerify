# pages/urls.py
from django.urls import path
from .views import CompanyDetailView, DepartmentDetailView, HomePageView

urlpatterns = [
    path('company/<int:pk>/department/<int:pk1>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'), # new
    path( '', HomePageView.as_view(), name='home' ),
]
