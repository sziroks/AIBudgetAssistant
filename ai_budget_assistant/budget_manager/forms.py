from django import forms
from datetime import datetime

from .models import MonthlyBudget
from .consts import (
    MODEL_MONTHLY_BUDGET_ID_MONTHLY_BUDGET,
    MODEL_MONTHLY_BUDGET_ID_APP_USER,
    MODEL_MONTHLY_BUDGET_MONTH,
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
