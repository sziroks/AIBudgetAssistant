# Generated by Django 5.0.3 on 2024-05-02 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_manager', '0004_alter_monthlybudget_debt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlybudget',
            options={'verbose_name_plural': 'Monthly Budgets'},
        ),
        migrations.RemoveField(
            model_name='account',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='monthlybudget',
            name='id_user',
        ),
        migrations.AddField(
            model_name='account',
            name='id_app_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='budget_manager.appuser'),
        ),
        migrations.AddField(
            model_name='monthlybudget',
            name='id_app_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='budget_manager.appuser'),
        ),
    ]