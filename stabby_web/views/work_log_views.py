import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from stabby_web.forms import WorkLogForm
from stabby_web.services import WorkLogService, KnifeService, SharpenerService
from stabby_web.enums import FormType, Module
from django.contrib.auth.decorators import login_required


@login_required
def work_log_create(request, related_entity_id):
    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        redirect_url = "knife-detail"
    else:
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)
        redirect_url = "sharpener-detail"

    if request.method == "POST":
        form = WorkLogForm(request.POST)
        if form.is_valid():
            wl = form.save(commit=False)
            WorkLogService.save_work_log(wl)
            messages.success(request, "Work Log Successfully Created!")
            return redirect(redirect_url, pk=related_entity_id) + "#work_log_card"

    else:
        initial = None
        module = None

        if "knives" in request.path:
            initial = {"knife": related_entity, "date": datetime.datetime.now()}
            module = Module.Knives.value
        else:
            initial = {"sharpener": related_entity, "date": datetime.datetime.now()}
            module = Module.Sharpeners.value

        form = WorkLogForm(initial)

        context = {
            "form": form,
            "form_type": FormType.Add.value,
            "related_entity": related_entity,
            "related_entity_id": related_entity_id,
            "active": module,
        }
        return render(request, "stabby_web/work-log-add-edit.html", context)


@login_required
def work_log_update(request, work_log_id, related_entity_id):
    wl = WorkLogService.get_work_log_detail(work_log_id)

    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        redirect_url = "knife-detail"
        module = Module.Knives.value
    else:
        redirect_url = "sharpener-detail"
        module = Module.Sharpeners.value
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)

    if request.method == "POST":
        form = WorkLogForm(request.POST)
        if form.is_valid():
            wl = form.save(commit=False)
            WorkLogService.save_work_log(wl)
            messages.success(request, "Work Log Successfully Created!")
            return redirect(redirect_url, pk=related_entity_id) + "#work_log_card"

    else:
        form = WorkLogForm(instance=wl)

        context = {
            "form": form,
            "form_type": FormType.Edit.value,
            "active": module,
            "related_entity": related_entity,
            "related_entity_id": related_entity_id,
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
