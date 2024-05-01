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


def get_all_accounts():
    return Account.objects.all()


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        accounts = get_all_accounts()
        return render(
            request,
            "budget_manager/landing_page.html",
            context={"accounts": accounts},
        )


class BudgetManagerView(View):
    def get(self, request, slug):
        id_account = Account.objects.get(slug=slug).id_account
        transactions = Transaction.objects.filter(id_account=id_account).order_by(
            "-time"
        )

        if request.GET:
            start_time = request.GET.get("start_date")
            end_time = request.GET.get("end_date")
            transaction_type = request.GET.get("transaction_type")

            if start_time:
                start_time = make_aware(datetime.strptime(start_time, "%Y-%m-%d"))
                transactions = transactions.filter(time__gte=start_time)

            if end_time:
                end_time = make_aware(datetime.strptime(end_time, "%Y-%m-%d")) + timedelta(days=1)
                transactions = transactions.filter(time__lt=end_time)

            if transaction_type:
                match transaction_type:
                    case "credit":
                        transactions = transactions.filter(amount__gt=0)
                    case "debit":
                        transactions = transactions.filter(amount__lt=0)
                    case _:
                        raise ValueError(
                            f"Invalid transaction type: {transaction_type}"
                        )

        context = {
            "transactions": transactions,
            "filter_form": TransactionFilterForm(request.GET),
        }
        return render(request, "budget_manager/budget_details.html", context=context)

    def post(self, request):
        print("post")
        print(request.POST)
        pass
