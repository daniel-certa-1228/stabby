from .models import (
    Sharpener,
    ViewKnifeGrid,
    ViewSharpenerGrid,
    Knife,
    ViewBladeGrid,
)


class DbService:

    @classmethod
    def get_blade_grid(self, knife_id):
        queryset = ViewBladeGrid.objects.filter(
            is_active=1, knife_id=knife_id
        ).order_by("is_main_blade", "-length")

        return list(queryset.values())

    @classmethod
    def get_knife_detail(self, knife_id):
        return Knife.objects.get(knife_id=knife_id)

    @classmethod
    def get_knife_grid(self):
        queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

        return list(queryset.values())

    @classmethod
    def get_sharpener_detail(self, sharpener_id):
        return Sharpener.objects.get(sharpener_id=sharpener_id)

    @classmethod
    def get_sharpener_grid(self):
        queryset = ViewSharpenerGrid.objects.filter(is_active=1).order_by(
            "brand", "sharpener", "cutting_agent"
        )

        return list(queryset.values())
