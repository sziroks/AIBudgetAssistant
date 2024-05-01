from django import forms


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
