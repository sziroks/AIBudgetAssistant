from django.contrib import admin

from .models import User, Currency, Account, Transaction

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("id_user",)
    list_display = (
        "id_user",
        "name",
        "lastname",
        "email",
    )


class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ("id_currency",)
    list_display = (
        "id_currency",
        "name",
        "short_name",
        "to_pln",
    )


class AccountAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = (
        "id_account",
    )
    list_display = (
        "id_account",
        "id_user",
        "name",
        "balance",
        "main_currency",
        "start_time",
        "end_time",
    )


class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ("id_transaction",)
    list_display = (
        "id_transaction",
        "id_account",
        "amount",
        "currency",
        "time",
        "description",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
