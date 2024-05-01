from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login/"