from django.contrib import admin
from django.urls import path, include
from .views import (
    landing_page,
    transactions,
    registration,
    logout,
)

urlpatterns = [
    path("", landing_page.LandingPageView.as_view(), name="landing_page"),
    path("register", registration.RegistrationView.as_view(), name="registration"),
    path("accounts/", include("django.contrib.auth.urls"), name="login-page"),
    path("logout", logout.logout_view, name="logout"),
    path(
        "<slug:slug>",
        transactions.TransactionView.as_view(),
        name="budget_manager",
    ),
]
