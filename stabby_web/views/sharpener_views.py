from django.http import JsonResponse
from django.contrib import messages
from stabby_web.forms import SharpenerForm
from stabby_web.services import SharpenerService
from django.shortcuts import render, redirect
from stabby_web.enums import FormType, Module


# MVT VIEWS
def sharpeners(request):
    context = {"active": Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


def sharpener_detail(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    context = {"active": Module.Sharpeners.value, "sharpener": sharpener}

    return render(request, "stabby_web/sharpener-detail.html", context)


def sharpener_create(request):
    if request.method == "POST":
        form = SharpenerForm(request.Post)
        if form.is_valid():
            sharpener = form.save(commit=False)
            sharpener.user = request.user
            SharpenerService.save_sharpener(sharpener)
            messages.success(request, "Sharpener Successfully Created!")
            return redirect("sharpener-detail", pk=sharpener.pk)

    else:
        form = SharpenerForm()
        context = {
            "form": form,
            "form_type": FormType.Add.value,
            "active": Module.Sharpeners.value,
        }
        return render(request, "stabby_web/sharpener-add-edit.html", context)


def sharpener_update(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    if request.method == "POST":
        form = SharpenerForm(request.Post)
        if form.is_valid():
            sharpener = form.save(commit=False)
            SharpenerService.save_sharpener(sharpener)
            messages.success(request, "Sharpener Successfully Updated!")
            return redirect("sharpener-detail", pk=sharpener.pk)

    else:
        form = SharpenerForm(instance=sharpener)
        context = {
            "form": form,
            "form_type": FormType.Edit.value,
            "active": Module.Sharpeners.value,
            "sharpener_id": sharpener_id,
        }
        return render(request, "stabby_web/sharpener-add-edit.html", context)


# JSON VIEWS
def get_sharpener_grid(request):
    data = SharpenerService.get_sharpener_grid()

    return JsonResponse(data, safe=False)
