from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import PhotoForm
from stabby_web.models import Knife, Sharpener
from stabby_web.services import (
    KnifeService,
    LibraryService,
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
def photo_create(request, related_entity_id=None):
    related_entity = None
    redirect_url = None

    if "knives" in request.path:
        related_entity = KnifeService.get_knife_detail(related_entity_id)
        redirect_url = "knife_detail"
    if "sharpeners" in request.path:
        related_entity = SharpenerService.get_sharpener_detail(related_entity_id)
        redirect_url = "sharpener_detail"
    else:
        related_entity = None
        redirect_url = "library"

    if request.method == "POST":
        now = TimeZoneService.get_now()

        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = None

            if type(related_entity) is Knife:
                photo = PhotoService.map_photo_form_data(form, now, related_entity)
            elif type(related_entity) is Sharpener:
                photo = PhotoService.map_photo_form_data(
                    form, now, None, related_entity
                )
            else:
                photo = PhotoService.map_photo_form_data(form, now, None, None)

            if request.is_collector:
                PhotoService.save_photo(photo)

            messages.success(request, "Photo Created!")

            if type(related_entity) is Knife:
                return redirect(redirect_url, knife_id=related_entity_id)
            elif type(related_entity) is Sharpener:
                return redirect(redirect_url, sharpener_id=related_entity_id)
            else:
                return redirect(redirect_url)
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
        elif type(related_entity) is Sharpener:
            initial = {"sharpener": related_entity}
            module = Modules.Sharpeners.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.SharpenerPhotoAddEdit.value,
                not settings.DEBUG,
                None,
                related_entity_id,
            )
        else:
            initial = None
            module = Modules.Library.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.LibraryItemAddEdit.value, not settings.DEBUGS
            )

        form = PhotoForm(initial, active=module)

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
        elif type(related_entity) is Sharpener:
            context["sharpener"] = related_entity
            context["sharpener_id"] = related_entity_id
        else:
            context["library"] = LibraryService.get_photos_grouped_by_brand()

        return render(request, "stabby_web/photo-add-edit.html", context)


@skip_save
@login_required
def photo_update(request, photo_id, related_entity_id=None):
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
    elif "sharpeners" in request.path:
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
    else:
        related_entity = None
        module = Modules.Library.value
        redirect_url = "library"
        variable_dto = TemplateVariableDTO(
            ViewTypes.LibraryItemAddEdit.value,
            not settings.DEBUG,
            None,
            None,
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
            elif type(related_entity) is Sharpener:
                photo = PhotoService.map_photo_form_data(
                    form, now, None, related_entity, photo
                )
            else:
                photo = PhotoService.map_photo_form_data(form, now, None, None, photo)

            if request.is_collector:
                PhotoService.save_photo(photo)

            messages.success(request, "Photo Updated!")

            if type(related_entity) is Knife:
                return redirect(redirect_url, knife_id=related_entity_id)
            elif type(related_entity) is Sharpener:
                return redirect(redirect_url, sharpener_id=related_entity_id)
            else:
                return redirect(redirect_url)
        else:
            messages.error(request, "Photo Update Failed")
    else:
        form = PhotoForm(instance=photo, active=module)

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
        elif type(related_entity) is Sharpener:
            context["sharpener"] = related_entity
            context["sharpener_id"] = related_entity_id
        else:
            context["library"] = LibraryService.get_photos_grouped_by_brand()

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
