from django.shortcuts import get_object_or_404
from ..models import (
    Blade,
    ViewBladeGrid,
)


class BladeService:

    @classmethod
    def get_blade_detail(self, blade_id):
        return get_object_or_404(Blade, blade_id=blade_id)

    @classmethod
    def get_blade_grid(self, knife_id):
        queryset = ViewBladeGrid.objects.filter(
            is_active=1, knife_id=knife_id
        ).order_by("is_main_blade", "-length")

        return list(queryset.values())

    @classmethod
    def save_blade(self, blade):
        return blade.save()
