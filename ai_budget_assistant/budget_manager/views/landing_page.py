from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from ..models import Account
from ..consts import (
    LANDING_PAGE_VIEW_CONTEXT_ACCOUNTS,
    TEMPLATE_LANDING_PAGE,
)


class LandingPageView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/accounts/login/")
        accounts = Account.objects.filter(id_user=request.user.id)
        return render(
            request,
            TEMPLATE_LANDING_PAGE,
            context={LANDING_PAGE_VIEW_CONTEXT_ACCOUNTS: accounts},
        )
