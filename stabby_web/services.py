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

    # @classmethod
    # def get_knife_detail(self, knife_id):
    #     knife = Knife.objects.get(knife_id=knife_id)

    #     if knife:
    #         knife_detail_dto = KnifeDetailDTO(
    #             knife_id=knife.knife_id,
    #             blade_material=(
    #                 knife.blade_material.name if knife.blade_material else None
    #             ),
    #             blade_material_notes=(
    #                 knife.blade_material.notes if knife.blade_material else None
    #             ),
    #             brand=knife.brand.name if knife.brand else None,
    #             brand_notes=knife.brand.notes if knife.brand else None,
    #             closed_length=knife.closed_length,
    #             country=knife.country.name if knife.country else None,
    #             deployment_type=(
    #                 knife.deployment_type.name if knife.deployment_type else None
    #             ),
    #             handle_material=(
    #                 knife.handle_material.name if knife.handle_material else None
    #             ),
    #             handle_material_notes=(
    #                 knife.handle_material_notes if knife.handle_material else None
    #             ),
    #             knife_type=knife.knife_type.name if knife.knife_type else None,
    #             knife_type_notes=knife.knife_type.notes if knife.knife_type else None,
    #             lock_type=knife.lock_type.name if knife.lock_type else None,
    #             lock_type_notes=knife.lock_type.notes if knife.lock_type else None,
    #             name=knife.name,
    #             needs_work=knife.needs_work,
    #             notes=knife.notes,
    #             purchased_new=knife.purchased_new,
    #             uom=knife.uom.name if knife.uom else None,
    #             vendor=knife.vendor.name if knife.vendor else None,
    #             year_of_manufacture=knife.year_of_manufacture,
    #             year_of_purchase=knife.year_of_purchase,
    #         )

    #         return knife_detail_dto
    #     else:
    #         return None
