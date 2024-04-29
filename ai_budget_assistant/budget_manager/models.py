from django.db import models


class User(models.Model):
    """
    Model for storing user information.
        * id_user - unique identifier of the user
        * name - first name of the user
        * lastname - last name of the user
        * email - email address of the user
    """

    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        """
        Sets the string representation of the user instance.
        """
        return f"{self.name} {self.lastname}"


class Currency(models.Model):
    """
    Model for storing currency information.
        * id_currency - unique identifier of the currency
        * name - full name of the currency
        * short_name - short name of the currency
        * to_pln - conversion rate from the currency to PLN
    """

    id_currency = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=3)
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
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    main_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Sets the string representation of the account instance.
        """
        return f"{self.name}"


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
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """
        Sets the string representation of the transaction instance.
        """
        return f"{self.id_account} {self.amount}"
