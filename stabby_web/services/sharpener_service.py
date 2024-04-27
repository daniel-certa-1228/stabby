from django.shortcuts import get_object_or_404
from ..models import (
    Sharpener,
    ViewSharpenerGrid,
)


class SharpenerService:

    @classmethod
    def get_sharpener_detail(self, sharpener_id):
        return get_object_or_404(Sharpener, sharpener_id=sharpener_id)

    @classmethod
    def get_sharpener_grid(self):
        queryset = ViewSharpenerGrid.objects.filter(is_active=1).order_by(
            "brand", "sharpener", "cutting_agent"
        )

        return list(queryset.values())

    @classmethod
    def save_sharpener(self, sharpener):
        return sharpener.save()
