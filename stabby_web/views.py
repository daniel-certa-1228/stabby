from django.http import JsonResponse
from django.shortcuts import render
from .services import DbService
from . import enums


# MVT Requests
def index(request):
    context = {"active": enums.Module.Knives.value}

    return render(request, "stabby_web/index.html", context)


def sharpeners(request):
    context = {"active": enums.Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


# JSON Requests
def get_knife_grid(request):
    data = DbService.get_knife_grid()

    return JsonResponse(data, safe=False)
