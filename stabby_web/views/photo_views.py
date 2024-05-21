import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import PhotoForm
from stabby_web.models import Knife
from stabby_web.services import KnifeService, SharpenerService, PhotoService
from stabby_web.enums import FormTypes, Modules, ViewTypes
from django.contrib.auth.decorators import login_required


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
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = None

            if type(related_entity) is Knife:
                photo = PhotoService.map_photo_form_data(form, related_entity)
            else:
                photo = PhotoService.map_photo_form_data(form, None, related_entity)

            PhotoService.save_photo(photo)

            messages.success(request, "Photo Created!")

            if type(related_entity) is Knife:
                return redirect(redirect_url, knife_id=related_entity_id)
            else:
                return redirect(redirect_url, sharpener_id=related_entity_id)
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
                ViewTypes.KnifePhotoAddEdit.value, related_entity_id
            )
        else:
            initial = {"sharpener": related_entity}
            module = Modules.Sharpeners.value
            variable_dto = TemplateVariableDTO(
                ViewTypes.SharpenerPhotoAddEdit.value, None, related_entity_id
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
            None,
            related_entity_id,
            None,
            None,
            photo_id,
        )

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        print(form.data)
        print(form.files)

        if form.is_valid():
            if type(related_entity) is Knife:
                photo = PhotoService.map_photo_form_data(
                    form, related_entity, None, photo
                )
            else:
                photo = PhotoService.map_photo_form_data(
                    form, None, related_entity, photo
                )

            PhotoService.save_photo(photo)

            messages.success(request, "Photo Updated!")

            if type(related_entity) is Knife:
                return redirect(redirect_url, knife_id=related_entity_id)
            else:
                return redirect(redirect_url, sharpener_id=related_entity_id)
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
