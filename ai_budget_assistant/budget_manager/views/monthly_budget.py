from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect

from ..models import MonthlyBudget, AppUser, Account
from ..forms import MonthlyBudgetForm
from ..utils import get_app_user


class MonthlyBudgetView(LoginRequiredMixin, CreateView):
    model = MonthlyBudget
    form_class = MonthlyBudgetForm
    template_name = "budget_manager/monthly_budget.html"
    success_url = reverse_lazy("landing_page")

    def form_valid(self, form) -> HttpResponse:
        logged_user = get_app_user(self.request)
        form.instance.id_user = logged_user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("landing_page")


def monthly_budget_check_view(request, *args, **kwargs):
    logged_app_user = get_app_user(request)
    print(f"logged_user: {logged_app_user}")
    try:
        queryset = Account.objects.filter(id_app_user=logged_app_user)
        print(f"queryset: {queryset}")
        if not queryset.exists():
            print("tutaj")
            raise Http404("Object not found1")
    except Exception as e:
        raise Http404(f"Object not found\n{e}")

    return HttpResponseRedirect("monthly-budget")
