from django.http import JsonResponse
from ..services import KnifeService
from django.shortcuts import render
from ..enums import Module, FormType


# MVT VIEWS
def index(request):
    context = {"active": Module.Knives.value}

    return render(request, "stabby_web/index.html", context)


# def add_knife(request):
#     context = {"form_type": FormType.Add}

#     return render(request, "stabby_web/knife-add-edit.html", context)


# def edit_knife(request, knife_id):
#     context = {"form_type": FormType.Edit}

#     return render(request, "stabby_web/knife-add-edit.html", context)


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
