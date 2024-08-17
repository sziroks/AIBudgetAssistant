from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


def load_transactions(request, slug):
    if request.POST:
        uploaded_file = request.FILES.get("file")
        print(f"{uploaded_file}\n\n\n\n\n")
        if uploaded_file is None:
            print(
                reverse(
                    "budget_manager", args=[request.get_full_path()[1:].split("/")[0]]
                )
            )
            HttpResponseRedirect(
                reverse(
                    "budget_manager", args=[request.get_full_path()[1:].split("/")[0]]
                )
            )
        return HttpResponse("abc")
    return HttpResponseRedirect(
        reverse("budget_manager", args=[request.get_full_path()[1:].split("/")[0]])
    )
