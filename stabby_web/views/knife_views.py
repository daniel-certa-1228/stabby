import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.enums import Modules, FormTypes, UnitsOfMeasure, ViewTypes
from stabby_web.forms import KnifeForm
from stabby_web.services import KnifeService
from django.contrib.auth.decorators import login_required


# MVT VIEWS
@login_required
def index(request):
    variable_dto = TemplateVariableDTO(
        ViewTypes.KnifeGrid.value
    )

    context = {
        "active": Modules.Knives.value,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/index.html", context)


@login_required
def knife_create(request):
    if request.method == "POST":
        form = KnifeForm(request.POST)

        if form.is_valid():
            knife = KnifeService.map_knife_form_data(request, form)

            KnifeService.save_knife(knife)

            messages.success(request, "Knife Created!")

            return redirect("knife_detail", knife_id=knife.knife_id)
        else:
            messages.error(request, "Knife Create Failed.")

    else:
        form = KnifeForm(
            initial={"uom": UnitsOfMeasure.inches.value, "purchased_new": True}
        )

        variable_dto = TemplateVariableDTO(
            ViewTypes.KnifeAddEdit.value
        )

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": Modules.Knives.value,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/knife-add-edit.html", context)


@login_required
def knife_detail(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    number_of_blades = knife.number_of_blades()

    variable_dto = TemplateVariableDTO(
        ViewTypes.KnifeDetail.value, knife_id
    )

    context = {
        "active": Modules.Knives.value,
        "knife": knife,
        "number_of_blades": number_of_blades,
        "template_variables": variable_dto.to_dict(),
    }

    return render(request, "stabby_web/knife-detail.html", context)


@login_required
def knife_update(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    if request.method == "POST":
        form = KnifeForm(request.POST)

        if form.is_valid():
            KnifeService.save_knife(
                KnifeService.map_knife_form_data(request, form, knife)
            )

            messages.success(request, "Knife Updated!")

        else:
            messages.error(request, "Knife Update Failed.")

        return redirect("knife_detail", knife_id=knife.knife_id)
    else:
        form = KnifeForm(instance=knife)

        variable_dto = TemplateVariableDTO(
            ViewTypes.KnifeAddEdit.value, knife_id
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
@login_required
def get_knife_grid(request):
    data = KnifeService.get_knife_grid()

    return JsonResponse(data, safe=False)


@login_required
def knife_delete(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    KnifeService.save_knife(KnifeService.delete_knife(knife))

    messages.success(request, "Knife Deleted")

    return JsonResponse(True, safe=False)
