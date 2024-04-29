from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import User, Account, Currency, Transaction
from .forms import TransactionsUploadForm


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        accounts = Account.objects.all()
        transaction_form = TransactionsUploadForm()
        return render(
            request,
            "budget_manager/landing_page.html",
            context={"accounts": accounts, "file_upload": transaction_form},
        )
