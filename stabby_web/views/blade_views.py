from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import FormTypes, Modules, ViewTypes
from stabby_web.forms import BladeForm
from stabby_web.services import BladeService, KnifeService, TimeZoneService
from django.contrib.auth.decorators import login_required
from stabby_web.decorators import skip_save


# MVT VIEWS
@skip_save
@login_required
def blade_create(request, knife_id: int):
    knife = KnifeService.get_knife_detail(knife_id)

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = BladeForm(request.POST)

        if form.is_valid():
            blade = BladeService.map_blade_form_to_data(request, form, now, knife)

            if request.is_collector:
                BladeService.save_blade(blade)

            messages.success(request, "Blade Created!")

            return redirect("knife_detail", knife_id=blade.knife_id)
        else:
            messages.error(request, "Blade Create Failed.")

    else:
        form = BladeForm(initial={"knife": knife, "uom": knife.uom})

        number_of_blades = knife.number_of_blades()

        variable_dto = TemplateVariableDTO(
            ViewTypes.BladeAddEdit.value, not settings.DEBUG, knife_id
        )

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": Modules.Knives.value,
            "knife": knife,
            "number_of_blades": number_of_blades,
            "template_variables": variable_dto.to_dict(),
        }
        return render(request, "stabby_web/blade-add-edit.html", context)


@skip_save
@login_required
def blade_update(request, knife_id: int, blade_id: int):
    knife = KnifeService.get_knife_detail(knife_id)
    blade = BladeService.get_blade_detail(blade_id)

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = BladeForm(request.POST)

        if form.is_valid():
            if request.is_collector:
                BladeService.save_blade(
                    BladeService.map_blade_form_to_data(
                        request, form, now, knife, blade
                    )
                )

            messages.success(request, "Blade Updated!")

        else:
            messages.error(request, "Blade Update Failed.")

        return redirect("knife_detail", knife_id=blade.knife_id)
    else:
        blade.length = blade.length.normalize() if blade.length else None
        blade.length_cutting_edge = (
            blade.length_cutting_edge.normalize() if blade.length_cutting_edge else None
        )

        form = BladeForm(instance=blade)

        number_of_blades = knife.number_of_blades()

        variable_dto = TemplateVariableDTO(
            ViewTypes.BladeAddEdit.value, not settings.DEBUG, knife_id, None, blade_id
        )

        context = {
            "form": form,
            "form_type": FormTypes.Edit.value,
            "active": Modules.Knives.value,
            "knife": knife,
            "number_of_blades": number_of_blades,
            "template_variables": variable_dto.to_dict(),
        }

    return render(request, "stabby_web/blade-add-edit.html", context)


# JSON VIEWS
@skip_save
@login_required
def blade_delete(request, blade_id: int):
    blade = BladeService.get_blade_detail(blade_id)

    if request.is_collector:
        BladeService.save_blade(BladeService.delete_blade(blade))

    messages.success(request, "Blade Deleted")

    return JsonResponse(True, safe=False)


@login_required
def get_blade_grid(request, knife_id: int):
    data = BladeService.get_blade_grid(knife_id)

    return JsonResponse(data, safe=False)
