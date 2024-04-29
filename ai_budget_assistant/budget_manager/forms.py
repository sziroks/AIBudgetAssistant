from django import forms

class TransactionsUploadForm(forms.Form):
    transactions = forms.FileField()