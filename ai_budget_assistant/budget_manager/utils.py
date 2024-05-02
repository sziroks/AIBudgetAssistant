from .models import AppUser


def get_app_user(request):
    return AppUser.objects.get(id_user=request.user)
