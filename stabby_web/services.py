from .models import ViewKnifeGrid


class DbService:

    @classmethod
    def get_knife_grid(self):
        queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

        return list(queryset.values())
