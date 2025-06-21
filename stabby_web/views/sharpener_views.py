from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import SharpenerForm
from stabby_web.services import SharpenerService, TimeZoneService
from django.shortcuts import render, redirect
from stabby_web.enums import FormTypes, Modules, UnitsOfMeasure, ViewTypes
from django.contrib.auth.decorators import login_required
from stabby_web.decorators import skip_save


# MVT VIEWS
@skip_save
@login_required
def sharpener_create(request):
    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = SharpenerForm(request.POST)

        if form.is_valid():
            sharpener = SharpenerService.map_sharpener_form_data(request, form, now)

            if request.is_collector:
                SharpenerService.save_sharpener(sharpener)

            messages.success(request, "Sharpener Created!")

            if request.is_collector:
                return redirect("sharpener_detail", sharpener_id=sharpener.sharpener_id)
            else:
                return redirect("sharpeners")
        else:
            messages.error(request, "Sharpener Create Failed.")

    else:
        form = SharpenerForm(initial={"uom": UnitsOfMeasure.inches.value})

        variable_dto = TemplateVariableDTO(
            ViewTypes.SharpenerAddEdit.value, not settings.DEBUG
        )

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": Modules.Sharpeners.value,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/sharpener-add-edit.html", context)


@login_required
def sharpener_detail(request, sharpener_id: int):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id, True)

    photos = sharpener.photos.all()

    variable_dto = TemplateVariableDTO(
        ViewTypes.SharpenerDetail.value, not settings.DEBUG, None, sharpener_id
    )

    context = {
        "active": Modules.Sharpeners.value,
        "sharpener": sharpener,
        "photos": photos,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/sharpener-detail.html", context)


@skip_save
@login_required
def sharpener_update(request, sharpener_id: int):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = SharpenerForm(request.POST)

        if form.is_valid():
            if request.is_collector:
                SharpenerService.save_sharpener(
                    SharpenerService.map_sharpener_form_data(
                        request, form, now, sharpener
                    )
                )

            messages.success(request, "Sharpener Updated!")

        else:
            messages.error(request, "Sharpener Update Failed.")

        return redirect("sharpener_detail", sharpener_id=sharpener.sharpener_id)
    else:
        sharpener.length = sharpener.length.normalize() if sharpener.length else None
        sharpener.width = sharpener.width.normalize() if sharpener.width else None

        form = SharpenerForm(instance=sharpener)

        variable_dto = TemplateVariableDTO(
            ViewTypes.SharpenerAddEdit.value, not settings.DEBUG, None, sharpener_id
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
    variable_dto = TemplateVariableDTO(
        ViewTypes.SharpenerGrid.value, not settings.DEBUG
    )

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


@skip_save
@login_required
def sharpener_delete(request, sharpener_id: int):
    sharpener = SharpenerService.get_sharpener_detail(sharpener_id)

    if request.is_collector:
        SharpenerService.save_sharpener(SharpenerService.delete_sharpener(sharpener))

    messages.success(request, "Sharpener Deleted")

    return JsonResponse(True, safe=False)
