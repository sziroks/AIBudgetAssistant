from django import forms
from datetime import datetime

from .models import (
    MonthlyBudget,
    Account,
    Currency,
)
from .consts import (
    MODEL_MONTHLY_BUDGET_ID_MONTHLY_BUDGET,
    MODEL_MONTHLY_BUDGET_ID_APP_USER,
    MODEL_MONTHLY_BUDGET_MONTH,
    MODEL_ACCOUNT_ID_ACCOUNT,
    MODEL_ACCOUNT_SLUG,
    MODEL_ACCOUNT_ID_APP_USER,
    MODEL_ACCOUNT_MAIN_CURRENCY,
    MODEL_ACCOUNT_NAME,
    MODEL_ACCOUNT_BALANCE,
    MODEL_ACCOUNT_START_TIME,
    MODEL_ACCOUNT_END_TIME,
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import BaseUserCreationForm


class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class TransactionFilterForm(forms.Form):
    start_date = forms.DateField(
        label="Start Date",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = forms.DateField(
        label="End Date",
        required=False,
        widget=forms.DateInput(
            attrs={"type": "date"},
        ),
    )
    transaction_type = forms.ChoiceField(
        label="Transaction Type",
        required=False,
        choices=(("", "All"), ("credit", "Credit"), ("debit", "Debit")),
    )


class MonthlyBudgetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[MODEL_MONTHLY_BUDGET_MONTH].initial = datetime.now().strftime("%B")

    class Meta:
        model = MonthlyBudget
        exclude = (
            MODEL_MONTHLY_BUDGET_ID_MONTHLY_BUDGET,
            MODEL_MONTHLY_BUDGET_ID_APP_USER,
        )


class AddAccountForm(forms.ModelForm):
    start_time = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    end_time = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[MODEL_ACCOUNT_MAIN_CURRENCY].initial = Currency.objects.get(
            short_name="PLN"
        )

    class Meta:
        model = Account
        labels = {
            MODEL_ACCOUNT_NAME: "Account Name",
            MODEL_ACCOUNT_BALANCE: "Account Balance",
            MODEL_ACCOUNT_MAIN_CURRENCY: "Account Currency",
            MODEL_ACCOUNT_START_TIME: "Start Date",
            MODEL_ACCOUNT_END_TIME: "End Date",
        }
        
        exclude = (
            MODEL_ACCOUNT_ID_ACCOUNT,
            MODEL_ACCOUNT_SLUG,
            MODEL_ACCOUNT_ID_APP_USER,
        )
