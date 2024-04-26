from django.http import JsonResponse
from ..services import KnifeService
from django.shortcuts import render
from ..enums import Module


# MVT VIEWS
def index(request):
    context = {"active": Module.Knives.value}

    return render(request, "stabby_web/index.html", context)


def knife_detail(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    number_of_blades = knife.number_of_blades()

    context = {
        "active": Module.Knives.value,
        "knife": knife,
        "number_of_blades": number_of_blades,
    }

    return render(request, "stabby_web/knife-detail.html", context)


# JSON VIEWS
def get_knife_grid(request):
    data = KnifeService.get_knife_grid()

    return JsonResponse(data, safe=False)
