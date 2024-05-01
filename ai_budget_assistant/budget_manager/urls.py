from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing_page"),
    path("<slug:slug>", views.BudgetManagerView.as_view(), name="budget_manager"),
]
