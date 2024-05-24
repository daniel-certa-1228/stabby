from django.db.models import F, Value, CharField
from django.db.models.functions import Coalesce, Concat

from ..models import (
    BladeMaterial,
    BladeShape,
    BondingAgent,
    Brand,
    Country,
    CuttingAgent,
    DeploymentType,
    HandleMaterial,
    KnifeType,
    LockType,
    Lubricant,
    SteelManufacturer,
    SteelType,
    UnitOfMeasure,
    Vendor,
)


class DropdownService:

    @classmethod
    def get_blade_materials(cls):
        return (
            BladeMaterial.objects.filter(is_active=True)
            .annotate(
                composite_name=Concat(
                    Coalesce(F("steel_manufacturer__name"), Value("")),
                    Value(" "),
                    F("name"),
                    output_field=CharField(),
                )
            )
            .order_by("composite_name")
        )

    @classmethod
    def get_blade_shapes(cls):
        return BladeShape.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_bonding_agents(cls):
        return BondingAgent.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_brands(cls):
        return Brand.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_countries(cls):
        return Country.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_cutting_agents(cls):
        return CuttingAgent.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_deployment_types(cls):
        return DeploymentType.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_handle_materials(cls):
        return HandleMaterial.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_knife_types(cls):
        return KnifeType.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_lock_types(cls):
        return LockType.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_lubricants(cls):
        return Lubricant.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_steel_manufacturers(cls):
        return SteelManufacturer.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_steel_types(cls):
        return SteelType.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_units_of_measure(cls):
        return UnitOfMeasure.objects.filter(is_active=True).order_by("name")

    @classmethod
    def get_vendors(cls):
        return Vendor.objects.filter(is_active=True).order_by("name")
