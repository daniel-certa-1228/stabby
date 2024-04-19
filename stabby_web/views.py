from django.http import JsonResponse
from django.shortcuts import get_list_or_404, render
from .models import ViewKnifeGrid
from . import enums


def index(request):
    queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

    context = {"active": enums.Module.Knives.value, "knives": queryset}

    return render(request, "stabby_web/index.html", context)


def sharpeners(request):
    context = {"active": enums.Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


def get_knife_grid(request):
    queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

    return_data = list(queryset.values())

    return JsonResponse(return_data, safe=False)
