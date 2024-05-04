from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import (
    Sharpener,
    ViewSharpenerGrid,
)


class SharpenerService:

    @classmethod
    def delete_sharpener(self, sharpener):
        sharpener.is_active = False

        return sharpener

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
    def map_sharpener_form_data(self, request, form, sharpener=None):
        if sharpener == None:
            sharpener = Sharpener()
            sharpener.create_date = timezone.now()
            sharpener.user = request.user

        sharpener.edit_date = timezone.now()
        sharpener.name = form.cleaned_data["name"]
        sharpener.notes = form.cleaned_data["notes"]
        sharpener.brand = form.cleaned_data["brand"]
        sharpener.brand_notes = form.cleaned_data["brand_notes"]
        sharpener.length = form.cleaned_data["length"]
        sharpener.width = form.cleaned_data["width"]
        sharpener.country = form.cleaned_data["country"]
        sharpener.cutting_agent = form.cleaned_data["cutting_agent"]
        sharpener.bonding_agent = form.cleaned_data["bonding_agent"]
        sharpener.lubricant = form.cleaned_data["lubricant"]
        sharpener.uom = form.cleaned_data["uom"]

        return sharpener

    @classmethod
    def save_sharpener(self, sharpener):
        return sharpener.save()
