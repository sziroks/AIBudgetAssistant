from django import forms
from datetime import datetime

from .models import MonthlyBudget
from .consts import (
    MODEL_MONTHLY_BUDGET_ID_MONTHLY_BUDGET,
    MODEL_MONTHLY_BUDGET_ID_USER,
    MODEL_MONTHLY_BUDGET_MONTH,
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
            MODEL_MONTHLY_BUDGET_ID_USER,
        )
        
