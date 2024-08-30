from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from stabby_web.dtos.knife_filter_dto import KnifeFilterDTO
from stabby_web.models import Blade, Knife, Photo, ViewKnifeGrid


class KnifeService:

    @classmethod
    def copy_knife(cls, knife_id, now):
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
    def delete_knife(cls, knife):
        knife.is_active = False

        return knife

    @classmethod
    def get_knife_detail(cls, knife_id, include_photos=False):
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
    def get_knife_grid(cls):
        queryset = ViewKnifeGrid.objects.filter(is_active=True).order_by(
            "brand", "knife"
        )

        return list(queryset.values())

    @classmethod
    def set_knife_filter(cls, request):
        brand = request.GET.get("brand")
        vendor = request.GET.get("vendor")
        blade_material = request.GET.get("blade_material")

        if brand or vendor or blade_material:
            if brand:
                dto = KnifeFilterDTO(brand=brand)
            elif vendor:
                dto = KnifeFilterDTO(vendor=vendor)
            elif blade_material:
                dto = KnifeFilterDTO(blade_material=blade_material)

            return dto
        else:
            return None

    @classmethod
    def save_knife(cls, knife):
        return knife.save()

    @classmethod
    def map_knife_form_data(cls, request, form, now, knife=None):
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
