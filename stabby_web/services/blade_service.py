from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import (
    Blade,
    ViewBladeGrid,
)


class BladeService:

    @classmethod
    def delete_blade(self, blade):
        blade.is_active = False

        return blade

    @classmethod
    def get_blade_detail(self, blade_id):
        return get_object_or_404(Blade, blade_id=blade_id)

    @classmethod
    def get_blade_grid(self, knife_id):
        queryset = ViewBladeGrid.objects.filter(
            is_active=1, knife_id=knife_id
        ).order_by("-is_main_blade", "-length")

        return list(queryset.values())

    @classmethod
    def map_blade_form_to_data(self, request, form, knife=None, blade=None):
        if blade == None:
            blade = Blade()
            blade.create_date = timezone.now()
            blade.user = request.user
            blade.knife = knife

        blade.edit_date = timezone.now()
        blade.length = form.cleaned_data["length"]
        blade.length_cutting_edge = form.cleaned_data["length_cutting_edge"]
        blade.uom = form.cleaned_data["uom"]
        blade.blade_shape = form.cleaned_data["blade_shape"]
        blade.blade_shape_notes = form.cleaned_data["blade_shape_notes"]
        blade.has_half_stop = form.cleaned_data["has_half_stop"]
        blade.is_main_blade = form.cleaned_data["is_main_blade"]

        return blade

    @classmethod
    def save_blade(self, blade):
        return blade.save()
