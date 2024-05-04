from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from stabby_web.enums import Module, FormType, UnitsOfMeasure
from stabby_web.forms import KnifeForm
from stabby_web.services import KnifeService
from django.contrib.auth.decorators import login_required


# MVT VIEWS
@login_required
def index(request):
    context = {"active": Module.Knives.value}

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

        context = {
            "form": form,
            "form_type": FormType.Add.value,
            "active": Module.Knives.value,
        }

        return render(request, "stabby_web/knife-add-edit.html", context)


@login_required
def knife_detail(request, knife_id):
    knife = KnifeService.get_knife_detail(knife_id)

    number_of_blades = knife.number_of_blades()

    context = {
        "active": Module.Knives.value,
        "knife": knife,
        "number_of_blades": number_of_blades,
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

        context = {
            "form": form,
            "form_type": FormType.Edit.value,
            "active": Module.Knives.value,
            "knife_id": knife_id,
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
