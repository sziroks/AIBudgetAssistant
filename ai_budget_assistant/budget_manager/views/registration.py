from django.views.generic import FormView

from ..models import AppUser
from ..forms import ExtendedUserCreationForm


class RegistrationView(FormView):
    form_class = ExtendedUserCreationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login/"
    

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            app_user_instance = AppUser(
                id_user=form.instance,
                name=form.instance.first_name,
                lastname=form.instance.last_name,
                email=form.instance.email,
            )
            app_user_instance.save()

        return super().form_valid(form)
