from django.contrib.auth import logout
from django.http import HttpResponseRedirect


def logout_view(request):
    if request.POST:
        logout(request)
        return HttpResponseRedirect("/accounts/login/")