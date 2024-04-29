from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from stabby_web.enums import FormType, Module
from stabby_web.forms import BladeForm
from stabby_web.services import BladeService
from stabby_web.services.knife_service import KnifeService
from django.contrib.auth.decorators import login_required


# MVT VIEWS


@login_required
def blade_create(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    if request.method == "POST":
        form = BladeForm(request.Post)
        if form.is_valid():
            blade = form.save(commit=False)
            BladeService.save_blade(blade)
            messages.success(request, "Blade Successfully Created!")
            return redirect("knife-detail", pk=blade.knife_id)

    else:
        form = BladeForm(initial={"knife": knife, "uom": knife.uom})

        number_of_blades = knife.number_of_blades()

        context = {
            "form": form,
            "form_type": FormType.Add.value,
            "active": Module.Knives.value,
            "knife": knife,
            "number_of_blades": number_of_blades,
        }
        return render(request, "stabby_web/blade-add-edit.html", context)


@login_required
def blade_update(request, knife_id, blade_id):
    knife = KnifeService.get_knife_detail(knife_id)
    blade = BladeService.get_blade_detail(blade_id)
    # is_main_cache = blade.is_main_blade

    if request.method == "POST":
        form = BladeForm(request.Post)
        if form.is_valid():
            blade = form.save(commit=False)
            BladeService.save_blade(blade)
            messages.success(request, "Blade Successfully Updated!")
            return redirect("knife-detail", pk=blade.knife_id)
    else:
        form = BladeForm(instance=blade)

        number_of_blades = knife.number_of_blades()

        context = {
            "form": form,
            "form_type": FormType.Edit.value,
            "active": Module.Knives.value,
            "knife": knife,
            "number_of_blades": number_of_blades,
        }

    return render(request, "stabby_web/blade-add-edit.html", context)


# JSON VIEWS
@login_required
def get_blade_grid(request, knife_id):
    data = BladeService.get_blade_grid(knife_id)

    return JsonResponse(data, safe=False)
