from django.contrib import admin

from .models import User, Currency, Account, Transaction
from .consts import (
    MODEL_USER_ID_USER,
    MODEL_USER_NAME,
    MODEL_USER_LASTNAME,
    MODEL_USER_EMAIL,
    MODEL_CURRENCY_ID_CURRENCY,
    MODEL_CURRENCY_NAME,
    MODEL_CURRENCT_SHORT_NAME,
    MODEL_CURRENCY_TO_PLN,
    MODEL_ACCOUNT_ID_ACCOUNT,
    MODEL_ACCOUNT_ID_USER,
    MODEL_ACCOUNT_NAME,
    MODEL_ACCOUNT_BALANCE,
    MODEL_ACCOUNT_MAIN_CURRENCY,
    MODEL_ACCOUNT_START_TIME,
    MODEL_ACCOUNT_END_TIME,
    MODEL_TRANSACTION_ID_TRANSACTION,
    MODEL_TRANSACTION_ID_ACCOUNT,
    MODEL_TRANSACTION_AMOUNT,
    MODEL_TRANSACTION_CURRENCY,
    MODEL_TRANSACTION_TIME,
    MODEL_TRANSACTION_DESCRIPTION,
)

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    readonly_fields = (MODEL_USER_ID_USER,)
    list_display = (
        MODEL_USER_ID_USER,
        MODEL_USER_NAME,
        MODEL_USER_LASTNAME,
        MODEL_USER_EMAIL,
    )


class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = (MODEL_CURRENCY_ID_CURRENCY,)
    list_display = (
        MODEL_CURRENCY_ID_CURRENCY,
        MODEL_CURRENCY_NAME,
        MODEL_CURRENCT_SHORT_NAME,
        MODEL_CURRENCY_TO_PLN,
    )


class AccountAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (MODEL_ACCOUNT_NAME,)}
    readonly_fields = (MODEL_ACCOUNT_ID_ACCOUNT,)
    list_display = (
        MODEL_ACCOUNT_ID_ACCOUNT,
        MODEL_ACCOUNT_ID_USER,
        MODEL_ACCOUNT_NAME,
        MODEL_ACCOUNT_BALANCE,
        MODEL_ACCOUNT_MAIN_CURRENCY,
        MODEL_ACCOUNT_START_TIME,
        MODEL_ACCOUNT_END_TIME,
    )


class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = (MODEL_TRANSACTION_ID_TRANSACTION,)
    list_display = (
        MODEL_TRANSACTION_ID_TRANSACTION,
        MODEL_TRANSACTION_ID_ACCOUNT,
        MODEL_TRANSACTION_AMOUNT,
        MODEL_TRANSACTION_CURRENCY,
        MODEL_TRANSACTION_TIME,
        MODEL_TRANSACTION_DESCRIPTION,
    )


admin.site.register(User, UserAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
