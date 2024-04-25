from django.http import JsonResponse
from django.shortcuts import render
from .services import DbService
from . import enums


# MVT Requests
def index(request):
    context = {"active": enums.Module.Knives.value}

    return render(request, "stabby_web/index.html", context)


def knife_detail(request, knife_id):
    knife = DbService.get_knife_detail(knife_id)

    number_of_blades = knife.number_of_blades()

    context = {
        "active": enums.Module.Knives.value,
        "knife": knife,
        "number_of_blades": number_of_blades,
    }

    return render(request, "stabby_web/knife-detail.html", context)


def sharpeners(request):
    context = {"active": enums.Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


def sharpener_detail(request, sharpener_id):
    sharpener = DbService.get_sharpener_detail(sharpener_id)

    context = {"active": enums.Module.Sharpeners.value, "sharpener": sharpener}

    return render(request, "stabby_web/sharpener-detail.html", context)


# JSON Requests
def get_blade_grid(request, knife_id):
    data = DbService.get_blade_grid(knife_id)

    return JsonResponse(data, safe=False)


def get_knife_grid(request):
    data = DbService.get_knife_grid()

    return JsonResponse(data, safe=False)


def get_sharpener_grid(request):
    data = DbService.get_sharpener_grid()

    return JsonResponse(data, safe=False)


def get_knife_work_log_grid(request, knife_id):
    data = DbService.get_knife_work_log_grid(knife_id)

    return JsonResponse(data, safe=False)


def get_sharpener_work_log_grid(request, sharpener_id):
    data = DbService.get_sharpener_work_log_grid(sharpener_id)

    return JsonResponse(data, safe=False)
