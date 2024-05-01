from django.utils import timezone
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

    @classmethod
    def map_knife_form_data(self, request, form, knife=None):
        if knife == None:
            knife = Knife()
            knife.create_date = timezone.now()
            knife.user = request.user

        knife.edit_date = timezone.now()
        knife.name = form.cleaned_data["name"]
        knife.notes = form.cleaned_data["notes"]
        knife.brand = form.cleaned_data["brand"]
        knife.brand_notes = form.cleaned_data["brand_notes"]
        knife.closed_length = form.cleaned_data["closed_length"]
        knife.uom = form.cleaned_data["uom"]
        knife.year_of_manufacture = form.cleaned_data["year_of_manufacture"]
        knife.country = form.cleaned_data["country"]
        knife.vendor = form.cleaned_data["vendor"]
        knife.year_of_purchase = form.cleaned_data["year_of_purchase"]
        knife.purchased_new = form.cleaned_data["purchased_new"]
        knife.knife_type = form.cleaned_data["knife_type"]
        knife.knife_type_notes = form.cleaned_data["knife_type_notes"]
        knife.blade_material = form.cleaned_data["blade_material"]
        knife.blade_material_notes = form.cleaned_data["blade_material_notes"]
        knife.handle_material = form.cleaned_data["handle_material"]
        knife.handle_material_notes = form.cleaned_data["handle_material_notes"]
        knife.lock_type = form.cleaned_data["lock_type"]
        knife.lock_type_notes = form.cleaned_data["lock_type_notes"]
        knife.deployment_type = form.cleaned_data["deployment_type"]
        knife.needs_work = form.cleaned_data["needs_work"]

        return knife
