# Generated by Django 5.0.3 on 2024-04-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='currency',
            new_name='main_currency',
        ),
    ]
