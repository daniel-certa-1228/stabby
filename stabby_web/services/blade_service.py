from ..models import (
    ViewBladeGrid,
)


class BladeService:

    @classmethod
    def get_blade_grid(self, knife_id):
        queryset = ViewBladeGrid.objects.filter(
            is_active=1, knife_id=knife_id
        ).order_by("is_main_blade", "-length")

        return list(queryset.values())
