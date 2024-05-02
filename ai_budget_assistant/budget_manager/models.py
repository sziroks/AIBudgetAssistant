from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from string import punctuation

from .consts import (
    MODEL_USER_NAME_MAX_LENGTH,
    MODEL_USER_LAST_NAME_MAX_LENGTH,
    MODEL_CURRENCY_NAME_MAX_LENGTH,
    MODEL_CURRENCY_SHORT_NAME_MAX_LENGTH,
    MODEL_ACCOUNT_NAME_MAX_LENGTH,
    MODEL_ACCOUNT_SLUG_MAX_LENGTH,
    MODEL_TRANSACTION_DESCRIPTION_MAX_LENGTH,
    MODEL_MONTHLY_BUDGET_MONTH_MAX_LENGTH,
)


class AppUser(models.Model):
    """
    Model for storing user information.
        * id_user - unique identifier of the user
        * name - first name of the user
        * lastname - last name of the user
        * email - email address of the user
    """

    id_app_user = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=MODEL_USER_NAME_MAX_LENGTH)
    lastname = models.CharField(max_length=MODEL_USER_LAST_NAME_MAX_LENGTH)
    email = models.EmailField()

    def __str__(self):
        """
        Sets the string representation of the user instance.
        """
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name_plural = "App Users"


class Currency(models.Model):
    """
    Model for storing currency information.
        * id_currency - unique identifier of the currency
        * name - full name of the currency
        * short_name - short name of the currency
        * to_pln - conversion rate from the currency to PLN
    """

    id_currency = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MODEL_CURRENCY_NAME_MAX_LENGTH)
    short_name = models.CharField(max_length=MODEL_CURRENCY_SHORT_NAME_MAX_LENGTH)
    to_pln = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        """
        Sets the string representation of the currency instance.
        """
        return f"{self.short_name}"

    class Meta:
        verbose_name_plural = "Currencies"


class Account(models.Model):
    """
    Model for storing accounts.
    * id_account - unique identifier of the account
    * id_user - identifier of the user of the account
    * name - name of the account
    * balance - balance of the account
    * main_currency - identifier of the main currency of the account
    * start_time - start time of the account
    * end_time - end time of the account
    """

    id_account = models.AutoField(primary_key=True)
    id_app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=MODEL_ACCOUNT_NAME_MAX_LENGTH)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    main_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
    slug = models.SlugField(
        max_length=MODEL_ACCOUNT_SLUG_MAX_LENGTH, null=False, db_index=True, unique=True
    )

    def __str__(self):
        """
        Sets the string representation of the account instance.
        """
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Account, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("budget_manager", args=[self.slug])


class Transaction(models.Model):
    """
    Model for storing transactions.
    * id_transaction - unique identifier of the transaction
    * id_account - identifier of the account on which the transaction was made
    * amount - amount of the transaction
    * currency - identifier of the currency of the transaction
    * time - time of the transaction
    * description - description of the transaction
    """

    id_transaction = models.AutoField(primary_key=True)
    id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    time = models.DateTimeField()
    description = models.CharField(
        max_length=MODEL_TRANSACTION_DESCRIPTION_MAX_LENGTH, null=True, blank=True
    )

    def __str__(self):
        """
        Sets the string representation of the transaction instance.
        """
        return f"{self.id_account} {self.amount}"


class MonthlyBudget(models.Model):
    id_monthly_budget = models.AutoField(primary_key=True)
    id_app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    month = models.CharField(max_length=MODEL_MONTHLY_BUDGET_MONTH_MAX_LENGTH)
    main_income = models.PositiveIntegerField(null=True, default=0)
    secondary_income = models.PositiveIntegerField(null=True, default=0)
    groceries = models.PositiveIntegerField(null=True, default=0)
    rent = models.PositiveIntegerField(null=True, default=0)
    transportation = models.PositiveIntegerField(null=True, default=0)
    entertainment = models.PositiveIntegerField(null=True, default=0)
    debt = models.PositiveIntegerField(null=True, default=0)
    subscriptions = models.PositiveIntegerField(null=True, default=0)
    savings = models.PositiveIntegerField(null=True, default=0)
    other_spendings = models.PositiveIntegerField(null=True, default=0)

    def __str__(self) -> str:
        return f"{self.id_app_user} {self.month}"

    class Meta:
        verbose_name_plural = "Monthly Budgets"
