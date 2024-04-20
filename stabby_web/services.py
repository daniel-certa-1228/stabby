from .models import ViewKnifeGrid, ViewSharpenerGrid


class DbService:

    @classmethod
    def get_knife_grid(self):
        queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

        return list(queryset.values())

    @classmethod
    def get_sharpener_grid(self):
        queryset = ViewSharpenerGrid.objects.filter(is_active=1).order_by(
            "brand", "sharpener", "cutting_agent"
        )

        return list(queryset.values())
