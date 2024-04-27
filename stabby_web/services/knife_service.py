from django.shortcuts import get_object_or_404
from ..models import (
    ViewKnifeGrid,
    Knife,
)


class KnifeService:

    @classmethod
    def get_knife_detail(self, knife_id):
        return get_object_or_404(Knife, knife_id=knife_id)

    @classmethod
    def get_knife_grid(self):
        queryset = ViewKnifeGrid.objects.filter(is_active=1).order_by("brand", "knife")

        return list(queryset.values())

    @classmethod
    def save_knife(self, knife):
        return knife.save()
