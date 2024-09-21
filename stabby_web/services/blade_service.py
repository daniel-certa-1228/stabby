from django.shortcuts import get_object_or_404
from ..models import (
    Blade,
    BladeShape,
    ViewBladeGrid,
)


class BladeService:

    @classmethod
    def delete_blade(cls, blade):
        blade.is_active = False

        return blade

    @classmethod
    def get_blade_detail(cls, blade_id):
        return get_object_or_404(Blade, blade_id=blade_id)

    @classmethod
    def get_blade_grid(cls, knife_id):
        queryset = ViewBladeGrid.objects.filter(
            is_active=True, knife_id=knife_id
        ).order_by("-is_main_blade", "-length")

        return list(queryset.values())

    @classmethod
    def get_blade_shape_name(cls, blade_shape_id):
        try:
            blade_shape_id_int = int(blade_shape_id)
        except (TypeError, ValueError):
            return None

        blade_shape = get_object_or_404(BladeShape, blade_shape_id=blade_shape_id_int)

        if blade_shape and blade_shape.name:
            return blade_shape.name

        return None

    @classmethod
    def map_blade_form_to_data(cls, request, form, now, knife=None, blade=None):
        if blade == None:
            blade = Blade()
            blade.create_date = now
            blade.user = request.user
            blade.knife = knife

        blade.edit_date = now
        blade.length = form.cleaned_data["length"]
        blade.length_cutting_edge = form.cleaned_data["length_cutting_edge"]
        blade.uom = form.cleaned_data["uom"]
        blade.blade_shape = form.cleaned_data["blade_shape"]
        blade.blade_shape_notes = form.cleaned_data["blade_shape_notes"]
        blade.has_half_stop = form.cleaned_data["has_half_stop"]
        blade.is_main_blade = form.cleaned_data["is_main_blade"]

        return blade

    @classmethod
    def save_blade(cls, blade):
        return blade.save()
