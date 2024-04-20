from django.http import JsonResponse
from django.shortcuts import render
from .models import ViewKnifeGrid
from .services import DbService
from . import enums


# MVT Requests
def index(request):
    queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

    context = {"active": enums.Module.Knives.value, "knives": queryset}

    return render(request, "stabby_web/index.html", context)


def sharpeners(request):
    context = {"active": enums.Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


# JSON Requests
def get_knife_grid(request):
    data = DbService.get_knife_grid()

    return JsonResponse(data, safe=False)
