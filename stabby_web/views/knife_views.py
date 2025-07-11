from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import Modules, FormTypes, UnitsOfMeasure, ViewTypes
from stabby_web.forms import KnifeForm
from stabby_web.services import BladeService, KnifeService, TimeZoneService
from stabby_web.decorators import skip_save


# MVT VIEWS
@login_required
def knives(request):
    filter = KnifeService.set_knife_filter(request)

    variable_dto = TemplateVariableDTO(
        ViewTypes.KnifeGrid.value, not settings.DEBUG, knife_filter=filter
    )

    blade_shape_name = None
    new_or_used = None

    if (
        variable_dto
        and variable_dto.knife_filter
        and variable_dto.knife_filter.blade_shape_id
    ):
        blade_shape_name = BladeService.get_blade_shape_name(
            variable_dto.knife_filter.blade_shape_id
        )
    elif (
        variable_dto
        and variable_dto.knife_filter
        and variable_dto.knife_filter.purchased_new is not None
    ):
        new_or_used = "New" if variable_dto.knife_filter.purchased_new else "Used"

    context = {
        "active": Modules.Knives.value,
        "template_variables": variable_dto.to_dict(),
        "blade_shape_name": blade_shape_name,
        "new_or_used": new_or_used,
    }

    return render(request, "stabby_web/knives.html", context)


@skip_save
@login_required
def knife_create(request):
    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = KnifeForm(request.POST)

        if form.is_valid():
            knife = KnifeService.map_knife_form_data(request, form, now)

            if request.is_collector:
                KnifeService.save_knife(knife)

            messages.success(request, "Knife Created!")

            if request.is_collector:
                return redirect("knife_detail", knife_id=knife.knife_id)
            else:
                return redirect("knives")
        else:
            messages.error(request, "Knife Create Failed.")

    else:
        form = KnifeForm(
            initial={"uom": UnitsOfMeasure.inches.value, "purchased_new": True}
        )

        variable_dto = TemplateVariableDTO(
            ViewTypes.KnifeAddEdit.value, not settings.DEBUG
        )

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": Modules.Knives.value,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/knife-add-edit.html", context)


@login_required
def knife_detail(request, knife_id: int):
    knife = KnifeService.get_knife_detail(knife_id, True)

    photos = knife.photos.all()

    number_of_blades = knife.number_of_blades()

    variable_dto = TemplateVariableDTO(
        ViewTypes.KnifeDetail.value, not settings.DEBUG, knife_id
    )

    context = {
        "active": Modules.Knives.value,
        "knife": knife,
        "photos": photos,
        "number_of_blades": number_of_blades,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/knife-detail.html", context)


@skip_save
@login_required
def knife_update(request, knife_id: int):
    knife = KnifeService.get_knife_detail(knife_id)

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = KnifeForm(request.POST)

        if form.is_valid():
            if request.is_collector:
                KnifeService.save_knife(
                    KnifeService.map_knife_form_data(request, form, now, knife)
                )

            messages.success(request, "Knife Updated!")

        else:
            messages.error(request, "Knife Update Failed.")

        return redirect("knife_detail", knife_id=knife.knife_id)
    else:
        knife.closed_length = (
            knife.closed_length.normalize() if knife.closed_length else None
        )

        form = KnifeForm(instance=knife)

        variable_dto = TemplateVariableDTO(
            ViewTypes.KnifeAddEdit.value, not settings.DEBUG, knife_id
        )

        context = {
            "form": form,
            "form_type": FormTypes.Edit.value,
            "active": Modules.Knives.value,
            "knife_id": knife_id,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/knife-add-edit.html", context)


# JSON VIEWS
@skip_save
@login_required
def copy_knife(request, knife_id: int):
    now = TimeZoneService.get_now()

    new_knife = None

    if request.is_collector:
        new_knife = KnifeService.copy_knife(knife_id, now)

    if new_knife or not request.is_collector:
        messages.success(request, "Knife Copied!")
    else:
        messages.error(request, "Knife Copy Failed.")

    if new_knife and request.is_collector:
        id = new_knife.knife_id
    elif not new_knife and request.is_collector:
        id = -1
    else:
        id = knife_id

    return JsonResponse(id, safe=False)


@login_required
def get_knife_grid(request):
    data = KnifeService.get_knife_grid(request)

    return JsonResponse(data, safe=False)


@skip_save
@login_required
def knife_delete(request, knife_id: int):
    knife = KnifeService.get_knife_detail(knife_id)

    if request.is_collector:
        KnifeService.save_knife(KnifeService.delete_knife(knife))

    messages.success(request, "Knife Deleted")

    return JsonResponse(True, safe=False)
