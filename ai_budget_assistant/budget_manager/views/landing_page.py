from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Account
from ..consts import (
    LANDING_PAGE_VIEW_CONTEXT_ACCOUNTS,
    TEMPLATE_LANDING_PAGE,
)
from ..utils import get_app_user


class LandingPageView(LoginRequiredMixin, View):
    def get(self, request):
        logged_app_user = get_app_user(self.request)
        accounts = Account.objects.filter(id_app_user=logged_app_user)
        return render(
            request,
            TEMPLATE_LANDING_PAGE,
            context={LANDING_PAGE_VIEW_CONTEXT_ACCOUNTS: accounts},
        )
