from django.contrib import admin
from django.urls import path, include
from .views import (
    landing_page,
    transactions,
    registration,
    logout,
    monthly_budget,
    add_account,
    load_transactions,
)

urlpatterns = [
    path("", landing_page.LandingPageView.as_view(), name="landing_page"),
    path("register", registration.RegistrationView.as_view(), name="registration"),
    path("accounts/", include("django.contrib.auth.urls"), name="login-page"),
    path("logout", logout.logout_view, name="logout"), # type: ignore
    path(
        "monthly-budget-check",
        monthly_budget.monthly_budget_check_view,
        name="monthly-budget-check",
    ),
    path(
        "monthly-budget",
        monthly_budget.MonthlyBudgetView.as_view(),
        name="monthly-budget",
    ),
    path("add-account", add_account.AddAccountView.as_view(), name="add-account"),
    path(
        "<slug:slug>",
        transactions.TransactionView.as_view(),
        name="budget_manager",
    ),
    path("<slug:slug>/load-transactions", view=load_transactions.load_transactions, name="load-transactions"),
]
