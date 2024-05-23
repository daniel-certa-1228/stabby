from django.http import JsonResponse
from django.contrib import messages
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import SharpenerForm
from stabby_web.services import SharpenerService
from django.shortcuts import render, redirect
from stabby_web.enums import FormTypes, Modules, UnitsOfMeasure, ViewTypes
from django.contrib.auth.decorators import login_required


# MVT VIEWS
@login_required
def sharpener_create(request):
    if request.method == "POST":
        form = SharpenerForm(request.POST)

        if form.is_valid():
            sharpener = SharpenerService.map_sharpener_form_data(request, form)

            SharpenerService.save_sharpener(sharpener)

            messages.success(request, "Sharpener Created!")

            return redirect("sharpener_detail", sharpener_id=sharpener.sharpener_id)
        else:
            messages.error(request, "Sharpener Create Failed.")

    else:
        form = SharpenerForm(initial={"uom": UnitsOfMeasure.inches.value})

        variable_dto = TemplateVariableDTO(ViewTypes.SharpenerAddEdit.value)

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": Modules.Sharpeners.value,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/sharpener-add-edit.html", context)


@login_required
def sharpener_detail(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id, True)

    photos = sharpener.photos.all()

    variable_dto = TemplateVariableDTO(
        ViewTypes.SharpenerDetail.value, None, sharpener_id
    )

    context = {
        "active": Modules.Sharpeners.value,
        "sharpener": sharpener,
        "photos": photos,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/sharpener-detail.html", context)


@login_required
def sharpener_update(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    if request.method == "POST":
        form = SharpenerForm(request.POST)
        if form.is_valid():
            SharpenerService.save_sharpener(
                SharpenerService.map_sharpener_form_data(request, form, sharpener)
            )

            messages.success(request, "Sharpener Updated!")

        else:
            messages.error(request, "Sharpener Update Failed.")

        return redirect("sharpener_detail", sharpener_id=sharpener.sharpener_id)
    else:
        form = SharpenerForm(instance=sharpener)

        variable_dto = TemplateVariableDTO(
            ViewTypes.SharpenerAddEdit.value, None, sharpener_id
        )

        context = {
            "form": form,
            "form_type": FormTypes.Edit.value,
            "active": Modules.Sharpeners.value,
            "sharpener_id": sharpener_id,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/sharpener-add-edit.html", context)


@login_required
def sharpeners(request):
    variable_dto = TemplateVariableDTO(ViewTypes.SharpenerGrid.value)

    context = {
        "active": Modules.Sharpeners.value,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/sharpeners.html", context)


# JSON VIEWS
@login_required
def get_sharpener_grid(request):
    data = SharpenerService.get_sharpener_grid()

    return JsonResponse(data, safe=False)


@login_required
def sharpener_delete(request, sharpener_id):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    SharpenerService.save_sharpener(SharpenerService.delete_sharpener(sharpener))

    messages.success(request, "Sharpener Deleted")

    return JsonResponse(True, safe=False)
