from django.shortcuts import render
from . import enums


def index(request):
    context = {"active": enums.Module.Knives.value}

    return render(request, "stabby_web/index.html", context)


def sharpeners(request):
    context = {"active": enums.Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)
