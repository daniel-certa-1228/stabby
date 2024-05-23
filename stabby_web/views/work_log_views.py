import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import WorkLogForm
from stabby_web.models import Knife
from stabby_web.services import WorkLogService, KnifeService, SharpenerService
from stabby_web.enums import FormTypes, Modules, ViewTypes
from django.contrib.auth.decorators import login_required


# MVT Views
@login_required
def work_log_create(request, related_entity_id):
    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        redirect_url = "knife_detail"
    else:
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)
        redirect_url = "sharpener_detail"

    if request.method == "POST":
        form = WorkLogForm(request.POST)

        if form.is_valid():
            work_log = None

            if type(related_entity) is Knife:
                work_log = WorkLogService.map_work_log_form_to_data(
                    form, related_entity
                )
            else:
                work_log = WorkLogService.map_work_log_form_to_data(
                    form, None, related_entity
                )

            WorkLogService.save_work_log(work_log)

            messages.success(request, "Work Log Created!")

        else:
            messages.error(request, "Work Log Create Failed")
            
        if type(related_entity) is Knife:
            return redirect(redirect_url, knife_id=related_entity_id)
        else:
            return redirect(redirect_url, sharpener_id=related_entity_id)
    else:
        initial = None
        module = None
        show_existing = True
        variable_dto = None

        if type(related_entity) is Knife:
            show_existing = WorkLogService.show_work_log_card(related_entity_id)
            initial = {"knife": related_entity, "date": datetime.datetime.now()}
            module = Modules.Knives.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.KnifeWorkLogAddEdit.value, related_entity_id
            )
        else:
            show_existing = WorkLogService.show_work_log_card(None, related_entity_id)
            initial = {"sharpener": related_entity, "date": datetime.datetime.now()}
            module = Modules.Sharpeners.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.SharpenerWorkLogAddEdit.value, None, related_entity_id
            )

        form = WorkLogForm(initial)

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": module,
            "related_entity": related_entity,
            "related_entity_id": related_entity_id,
            "show_existing": show_existing,
            "template_variables": variable_dto.to_dict(),
        }
        return render(request, "stabby_web/work-log-add-edit.html", context)


@login_required
def work_log_update(request, work_log_id, related_entity_id):
    work_log = WorkLogService.get_work_log_detail(work_log_id)

    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        redirect_url = "knife_detail"
        module = Modules.Knives.value
        variable_dto = TemplateVariableDTO(
            ViewTypes.KnifeWorkLogAddEdit.value,
            related_entity_id,
            None,
            None,
            work_log_id,
        )
    else:
        redirect_url = "sharpener_detail"
        module = Modules.Sharpeners.value
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)
        variable_dto = TemplateVariableDTO(
            ViewTypes.SharpenerWorkLogAddEdit.value,
            None,
            related_entity_id,
            None,
            work_log_id,
        )

    if request.method == "POST":
        form = WorkLogForm(request.POST)

        if form.is_valid():
            if type(related_entity) is Knife:
                work_log = WorkLogService.map_work_log_form_to_data(
                    form, related_entity, None, work_log
                )
            else:
                work_log = WorkLogService.map_work_log_form_to_data(
                    form, None, related_entity, work_log
                )

            WorkLogService.save_work_log(work_log)

            messages.success(request, "Work Log Updated!")

        else:
            messages.error(request, "Work Log Update Failed")
            
        if type(related_entity) is Knife:
            return redirect(redirect_url, knife_id=related_entity_id)
        else:
            return redirect(redirect_url, sharpener_id=related_entity_id)
    else:
        form = WorkLogForm(instance=work_log)

        context = {
            "form": form,
            "form_type": FormTypes.Edit.value,
            "active": module,
            "related_entity": related_entity,
            "related_entity_id": related_entity_id,
            "show_existing": True,
            "template_variables": variable_dto.to_dict(),
        }

        return render(request, "stabby_web/work-log-add-edit.html", context)


# JSON VIEWS
@login_required
def get_knife_work_log_grid(request, knife_id):
    data = WorkLogService.get_knife_work_log_grid(knife_id)

    return JsonResponse(data, safe=False)


@login_required
def get_sharpener_work_log_grid(request, sharpener_id):
    data = WorkLogService.get_sharpener_work_log_grid(sharpener_id)

    return JsonResponse(data, safe=False)


@login_required
def work_log_delete(request, work_log_id):
    work_log = WorkLogService.get_work_log_detail(work_log_id)

    WorkLogService.save_work_log(WorkLogService.delete_work_log(work_log))

    messages.success(request, "Work Log Deleted")

    return JsonResponse(True, safe=False)
