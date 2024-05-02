from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import MonthlyBudget, AppUser
from ..forms import MonthlyBudgetForm


class MonthlyBudgetView(LoginRequiredMixin, CreateView):
    model = MonthlyBudget
    form_class = MonthlyBudgetForm
    template_name = "budget_manager/monthly_budget.html"
    success_url = reverse_lazy("landing_page")

    def form_valid(self, form):
        logged_user = AppUser.objects.get(id_user=self.request.user)
        print(f"request: {self.request.user}")
        print(f"logged: {logged_user}")
        form.instance.id_user = logged_user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('landing_page')