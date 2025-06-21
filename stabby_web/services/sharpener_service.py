import datetime
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from ..models import Sharpener, ViewSharpenerGrid, Photo


class SharpenerService:

    @classmethod
    def delete_sharpener(cls, sharpener: Sharpener):
        sharpener.is_active = False

        return sharpener

    @classmethod
    def get_sharpener_detail(cls, sharpener_id: int, include_photos: bool = False):
        if include_photos == True:
            photos_prefetch = Prefetch(
                "photos",
                queryset=Photo.objects.filter(is_active=True).order_by("create_date"),
            )

            return get_object_or_404(
                Sharpener.objects.prefetch_related(photos_prefetch),
                sharpener_id=sharpener_id,
            )
        else:
            return get_object_or_404(Sharpener, sharpener_id=sharpener_id)

    @classmethod
    def get_sharpener_grid(cls):
        queryset = cls.get_sharpener_queryset()

        return list(queryset.values())

    @classmethod
    def get_sharpener_queryset(cls):
        return ViewSharpenerGrid.objects.filter(is_active=True).order_by(
            "brand", "sharpener", "cutting_agent"
        )

    @classmethod
    def map_sharpener_form_data(
        cls, request, form, now: datetime, sharpener: Sharpener = None
    ):
        if sharpener == None:
            sharpener = Sharpener()
            sharpener.create_date = now
            sharpener.user = request.user

        sharpener.edit_date = now
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
    def save_sharpener(cls, sharpener):
        return sharpener.save()
