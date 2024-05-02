from django.http import JsonResponse
from django.contrib import messages
from stabby_web.forms import SharpenerForm
from stabby_web.services import SharpenerService
from django.shortcuts import render, redirect
from stabby_web.enums import FormType, Module, UnitsOfMeasure
from django.contrib.auth.decorators import login_required


# MVT VIEWS
@login_required
def sharpeners(request):
    context = {"active": Module.Sharpeners.value}

    return render(request, "stabby_web/sharpeners.html", context)


@login_required
def sharpener_detail(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    context = {"active": Module.Sharpeners.value, "sharpener": sharpener}

    return render(request, "stabby_web/sharpener-detail.html", context)


@login_required
def sharpener_create(request):
    if request.method == "POST":
        form = SharpenerForm(request.POST)

        if form.is_valid():
            sharpener = SharpenerService.map_sharpener_form_data(request, form)

            SharpenerService.save_sharpener(sharpener)

            messages.success(request, "Sharpener Successfully Created!")

            return redirect("sharpener_detail", sharpener_id=sharpener.sharpener_id)

    else:
        form = SharpenerForm(initial={"uom": UnitsOfMeasure.inches.value})

        context = {
            "form": form,
            "form_type": FormType.Add.value,
            "active": Module.Sharpeners.value,
        }

        return render(request, "stabby_web/sharpener-add-edit.html", context)


@login_required
def sharpener_update(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    if request.method == "POST":
        form = SharpenerForm(request.POST)
        if form.is_valid():
            SharpenerService.save_sharpener(
                SharpenerService.map_sharpener_form_data(request, form, sharpener)
            )

            messages.success(request, "Sharpener Successfully Updated!")

        else:
            messages.error(request, "Sharpener Update Failed.")

        return redirect("sharpener_detail", sharpener_id=sharpener.sharpener_id)
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
@login_required
def get_sharpener_grid(request):
    data = SharpenerService.get_sharpener_grid()

    return JsonResponse(data, safe=False)
