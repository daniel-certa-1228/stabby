from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from ..enums import Module, FormType
from ..forms import KnifeForm
from ..services import KnifeService


# MVT VIEWS
def index(request):
    context = {"active": Module.Knives.value}

    return render(request, "stabby_web/index.html", context)


def knife_create(request):
    if request.method == "POST":
        form = KnifeForm(request.Post)
        if form.is_valid():
            knife = form.save(commit=False)
            KnifeService.save_knife(knife)
            messages.success(request, "Knife Successfully Created!")
            return redirect("knife-detail", pk=knife.pk)

    else:
        form = KnifeForm()
        context = {
            "form": form,
            "form_type": FormType.Add.value,
            "active": Module.Knives.value,
        }
        return render(request, "stabby_web/knife-add-edit.html", context)


def knife_update(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    if request.method == "POST":
        form = KnifeForm(request.Post)
        if form.is_valid():
            knife = form.save(commit=False)
            KnifeService.save_knife(knife)
            messages.success(request, "Knife Successfully Updated!")
            return redirect("knife-detail", pk=knife.pk)
    else:
        form = KnifeForm(instance=knife)
        context = {
            "form": form,
            "form_type": FormType.Edit.value,
            "active": Module.Knives.value,
        }

    return render(request, "stabby_web/knife-add-edit.html", context)


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
