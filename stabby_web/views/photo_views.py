from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import PhotoForm
from stabby_web.models import Knife
from stabby_web.services import (
    KnifeService,
    SharpenerService,
    PhotoService,
    TimeZoneService,
)
from stabby_web.enums import FormTypes, Modules, ViewTypes
from django.contrib.auth.decorators import login_required
from stabby_web.decorators import skip_save


# MVT Views
@skip_save
@login_required
def photo_create(request, related_entity_id):
    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        redirect_url = "knife_detail"
    else:
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)
        redirect_url = "sharpener_detail"

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = None

            if type(related_entity) is Knife:
                photo = PhotoService.map_photo_form_data(form, now, related_entity)
            else:
                photo = PhotoService.map_photo_form_data(
                    form, now, None, related_entity
                )

            if request.is_collector:
                PhotoService.save_photo(photo)

            messages.success(request, "Photo Created!")

            if type(related_entity) is Knife:
                return redirect(redirect_url, knife_id=related_entity_id)
            else:
                return redirect(redirect_url, sharpener_id=related_entity_id)
        else:
            messages.error(request, "Photo Create Failed")
    else:
        initial = None
        module = None
        variable_dto = None
        number_of_blades = 0

        if type(related_entity) is Knife:
            number_of_blades = related_entity.number_of_blades()
            initial = {"knife": related_entity}
            module = Modules.Knives.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.KnifePhotoAddEdit.value, not settings.DEBUG, related_entity_id
            )
        else:
            initial = {"sharpener": related_entity}
            module = Modules.Sharpeners.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.SharpenerPhotoAddEdit.value,
                not settings.DEBUG,
                None,
                related_entity_id,
            )

        form = PhotoForm(initial)

        context = {
            "form": form,
            "form_type": FormTypes.Add.value,
            "active": module,
            "template_variables": variable_dto.to_dict(),
        }

        if type(related_entity) is Knife:
            context["knife"] = related_entity
            context["knife_id"] = related_entity_id
            context["number_of_blades"] = number_of_blades

        else:
            context["sharpener"] = related_entity
            context["sharpener_id"] = related_entity_id

        return render(request, "stabby_web/photo-add-edit.html", context)


@skip_save
@login_required
def photo_update(request, related_entity_id, photo_id):
    photo = PhotoService.get_photo_detail(photo_id)

    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        number_of_blades = related_entity.number_of_blades()
        module = Modules.Knives.value
        redirect_url = "knife_detail"
        variable_dto = TemplateVariableDTO(
            ViewTypes.KnifePhotoAddEdit.value,
            not settings.DEBUG,
            related_entity_id,
            None,
            None,
            None,
            photo_id,
        )
    else:
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)
        module = Modules.Sharpeners.value
        redirect_url = "sharpener_detail"
        variable_dto = TemplateVariableDTO(
            ViewTypes.SharpenerPhotoAddEdit.value,
            not settings.DEBUG,
            None,
            related_entity_id,
            None,
            None,
            photo_id,
        )

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = PhotoForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
            if type(related_entity) is Knife:
                photo = PhotoService.map_photo_form_data(
                    form, now, related_entity, None, photo
                )
            else:
                photo = PhotoService.map_photo_form_data(
                    form, now, None, related_entity, photo
                )

            if request.is_collector:
                PhotoService.save_photo(photo)

            messages.success(request, "Photo Updated!")

            if type(related_entity) is Knife:
                return redirect(redirect_url, knife_id=related_entity_id)
            else:
                return redirect(redirect_url, sharpener_id=related_entity_id)
        else:
            messages.error(request, "Photo Update Failed")
    else:
        form = PhotoForm(instance=photo)

        context = {
            "form": form,
            "form_type": FormTypes.Edit.value,
            "active": module,
            "photo": photo,
            "template_variables": variable_dto.to_dict(),
        }

        if type(related_entity) is Knife:
            context["knife"] = related_entity
            context["knife_id"] = related_entity_id
            context["number_of_blades"] = number_of_blades

        else:
            context["sharpener"] = related_entity
            context["sharpener_id"] = related_entity_id

        return render(request, "stabby_web/photo-add-edit.html", context)


# JSON VIEWS
@skip_save
@login_required
def photo_delete(request, photo_id):
    work_log = PhotoService.get_photo_detail(photo_id)

    if request.is_collector:
        PhotoService.save_photo(PhotoService.delete_photo(work_log))

    messages.success(request, "Photo Deleted")

    return JsonResponse(True, safe=False)
