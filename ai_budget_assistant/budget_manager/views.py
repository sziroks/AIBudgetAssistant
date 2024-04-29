from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        return render(request, "budget_manager/landing_page.html")
