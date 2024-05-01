from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.timezone import make_aware
from datetime import (
    datetime,
    timedelta,
)

from .models import User, Account, Currency, Transaction
from .forms import TransactionFilterForm
from .consts import (
    LANDING_PAGE_VIEW_CONTEXT_ACCOUNTS,
    BUDGET_MANAGER_VIEW_CONTEXT_TRANSACTIONS,
    BUDGET_MANAGER_VIEW_CONTEXT_FILTER_FORM,
    MODEL_TRANSACTION_TIME,
    REQUEST_KEY_START_DATE,
    REQUEST_KET_END_DATE,
    REQUEST_KEY_TRANSACTION_TYPE,
    REQUEST_VALUE_CREDIT,
    REQUEST_VALUE_DEBIT,
    TEMPLATE_LANDING_PAGE,
    TEMPLATE_BUDGET_DETAILS,
)


def get_all_accounts():
    return Account.objects.all()


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        accounts = get_all_accounts()
        return render(
            request,
            TEMPLATE_LANDING_PAGE,
            context={LANDING_PAGE_VIEW_CONTEXT_ACCOUNTS: accounts},
        )


class BudgetManagerView(View):
    def get(self, request, slug):
        id_account = Account.objects.get(slug=slug).id_account
        transactions = Transaction.objects.filter(id_account=id_account).order_by(
            f"-{MODEL_TRANSACTION_TIME}"
        )

        if request.GET:
            start_time = request.GET.get(REQUEST_KEY_START_DATE)
            end_time = request.GET.get(REQUEST_KET_END_DATE)
            transaction_type = request.GET.get(REQUEST_KEY_TRANSACTION_TYPE)

            if start_time:
                start_time = make_aware(datetime.strptime(start_time, "%Y-%m-%d"))
                transactions = transactions.filter(time__gte=start_time)

            if end_time:
                end_time = make_aware(
                    datetime.strptime(end_time, "%Y-%m-%d")
                ) + timedelta(days=1)
                transactions = transactions.filter(time__lt=end_time)

            if transaction_type:
                if transaction_type == REQUEST_VALUE_CREDIT:
                    transactions = transactions.filter(amount__gt=0)
                elif transaction_type == REQUEST_VALUE_DEBIT:
                    transactions = transactions.filter(amount__lt=0)
                else:
                    raise ValueError(f"Invalid transaction: {transaction_type}")

        context = {
            BUDGET_MANAGER_VIEW_CONTEXT_TRANSACTIONS: transactions,
            BUDGET_MANAGER_VIEW_CONTEXT_FILTER_FORM: TransactionFilterForm(request.GET),
        }
        return render(request, TEMPLATE_BUDGET_DETAILS, context=context)

    def post(self, request):
        print("post")
        print(request.POST)
        pass
