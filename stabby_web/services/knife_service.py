import datetime
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from stabby_web.dtos import KnifeFilterDTO
from stabby_web.models import Blade, Knife, Photo, ViewKnifeGrid, ViewKnifeBladeGrid


class KnifeService:

    @classmethod
    def copy_knife(cls, knife_id: int, now: datetime):
        try:
            original_knife = Knife.objects.get(knife_id=knife_id)
            original_blades = original_knife.blades.filter(is_active=True)

            with transaction.atomic():
                new_knife = Knife(
                    name=f"{original_knife.name} (Copy)",
                    notes=original_knife.notes,
                    brand=original_knife.brand,
                    brand_notes=original_knife.brand_notes,
                    closed_length=original_knife.closed_length,
                    uom=original_knife.uom,
                    year_of_manufacture=original_knife.year_of_manufacture,
                    country=original_knife.country,
                    vendor=original_knife.vendor,
                    year_of_purchase=original_knife.year_of_purchase,
                    purchased_new=original_knife.purchased_new,
                    knife_type=original_knife.knife_type,
                    knife_type_notes=original_knife.knife_type_notes,
                    blade_material=original_knife.blade_material,
                    blade_material_notes=original_knife.blade_material_notes,
                    handle_material=original_knife.handle_material,
                    handle_material_notes=original_knife.handle_material_notes,
                    lock_type=original_knife.lock_type,
                    lock_type_notes=original_knife.lock_type_notes,
                    deployment_type=original_knife.deployment_type,
                    needs_work=original_knife.needs_work,
                    is_active=original_knife.is_active,
                    user=original_knife.user,
                    create_date=now,
                    edit_date=now,
                )
                new_knife.save()

                for blade in original_blades:
                    new_blade = Blade(
                        knife=new_knife,
                        length=blade.length,
                        length_cutting_edge=blade.length_cutting_edge,
                        uom=blade.uom,
                        blade_shape=blade.blade_shape,
                        blade_shape_notes=blade.blade_shape_notes,
                        has_half_stop=blade.has_half_stop,
                        is_main_blade=blade.is_main_blade,
                        is_active=blade.is_active,
                        create_date=now,
                        edit_date=now,
                    )
                    new_blade.save()

            return new_knife

        except Knife.DoesNotExist:
            print(f"Knife with id {knife_id} does not exist.")
            return None

    @classmethod
    def delete_knife(cls, knife: Knife):
        knife.is_active = False

        return knife

    @classmethod
    def get_knife_detail(cls, knife_id: int, include_photos: bool = False):
        if include_photos:
            photos_prefetch = Prefetch(
                "photos",
                queryset=Photo.objects.filter(is_active=True).order_by("create_date"),
            )

            return get_object_or_404(
                Knife.objects.prefetch_related(photos_prefetch), knife_id=knife_id
            )
        else:
            return get_object_or_404(Knife, knife_id=knife_id)

    @classmethod
    def get_knife_grid(cls, request):
        blade_shape_id = request.GET.get("blade_shape_id")
        purchased_new = request.GET.get("purchased_new")

        try:
            blade_shape_id_int = int(blade_shape_id)
        except (TypeError, ValueError):
            blade_shape_id = None

        purchased_new_bool = None

        if purchased_new:
            purchased_new_bool = purchased_new.lower() == "true"

        if blade_shape_id is not None:
            queryset = ViewKnifeBladeGrid.objects.filter(
                is_active=True, blade_shape_id=blade_shape_id_int
            ).order_by("brand", "knife")
        elif purchased_new is not None:
            queryset = ViewKnifeGrid.objects.filter(
                is_active=True, purchased_new=purchased_new_bool
            ).order_by("brand", "knife")
        else:
            queryset = cls.get_knife_queryset()

        return list(queryset.values())

    @classmethod
    def get_knife_queryset(cls):
        return ViewKnifeGrid.objects.filter(is_active=True).order_by("brand", "knife")

    @classmethod
    def set_knife_filter(cls, request):
        brand = request.GET.get("brand")
        vendor = request.GET.get("vendor")
        blade_material = request.GET.get("blade_material")
        handle_material = request.GET.get("handle_material")
        knife_type = request.GET.get("knife_type")
        purchased_new = request.GET.get("purchased_new")
        blade_shape_id = request.GET.get("blade_shape_id")

        if (
            brand
            or vendor
            or blade_material
            or handle_material
            or knife_type
            or blade_shape_id
            or purchased_new
        ):
            if brand:
                dto = KnifeFilterDTO(brand=brand)
            elif vendor:
                dto = KnifeFilterDTO(vendor=vendor)
            elif blade_material:
                dto = KnifeFilterDTO(blade_material=blade_material)
            elif handle_material:
                dto = KnifeFilterDTO(handle_material=handle_material)
            elif knife_type:
                dto = KnifeFilterDTO(knife_type=knife_type)
            elif purchased_new:
                dto = KnifeFilterDTO(purchased_new=purchased_new.lower() == "true")
            elif blade_shape_id:
                dto = KnifeFilterDTO(blade_shape_id=blade_shape_id)

            return dto
        else:
            return None

    @classmethod
    def save_knife(cls, knife: Knife):
        return knife.save()

    @classmethod
    def map_knife_form_data(cls, request, form, now: datetime, knife: Knife = None):
        if knife == None:
            knife = Knife()
            knife.create_date = now
            knife.user = request.user

        knife.edit_date = now
        knife.name = form.cleaned_data["name"]
        knife.notes = form.cleaned_data["notes"]
        knife.brand = form.cleaned_data["brand"]
        knife.brand_notes = form.cleaned_data["brand_notes"]
        knife.closed_length = form.cleaned_data["closed_length"]
        knife.uom = form.cleaned_data["uom"]
        knife.year_of_manufacture = form.cleaned_data["year_of_manufacture"]
        knife.country = form.cleaned_data["country"]
        knife.vendor = form.cleaned_data["vendor"]
        knife.year_of_purchase = form.cleaned_data["year_of_purchase"]
        knife.purchased_new = form.cleaned_data["purchased_new"]
        knife.knife_type = form.cleaned_data["knife_type"]
        knife.knife_type_notes = form.cleaned_data["knife_type_notes"]
        knife.blade_material = form.cleaned_data["blade_material"]
        knife.blade_material_notes = form.cleaned_data["blade_material_notes"]
        knife.handle_material = form.cleaned_data["handle_material"]
        knife.handle_material_notes = form.cleaned_data["handle_material_notes"]
        knife.lock_type = form.cleaned_data["lock_type"]
        knife.lock_type_notes = form.cleaned_data["lock_type_notes"]
        knife.deployment_type = form.cleaned_data["deployment_type"]
        knife.needs_work = form.cleaned_data["needs_work"]

        return knife
