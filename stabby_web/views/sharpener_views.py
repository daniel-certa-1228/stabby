from django.http import JsonResponse
from ..services import SharpenerService
from django.shortcuts import render
from ..enums import Module


# MVT VIEWS
def sharpeners(request):
    context = {"active": Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


def sharpener_detail(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    context = {"active": Module.Sharpeners.value, "sharpener": sharpener}

    return render(request, "stabby_web/sharpener-detail.html", context)


# JSON VIEWS
def get_sharpener_grid(request):
    data = SharpenerService.get_sharpener_grid()

    return JsonResponse(data, safe=False)
