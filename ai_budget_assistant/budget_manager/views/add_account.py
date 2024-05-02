from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

from ..forms import AddAccountForm
from ..models import Account
from ..utils import get_app_user

class AddAccountView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AddAccountForm
    template_name = "budget_manager/add_account.html"
    success_url = reverse_lazy("landing_page")

    def form_valid(self, form) -> HttpResponse:
        logged_user = get_app_user(self.request)
        form.instance.id_app_user = logged_user
        return super().form_valid(form)