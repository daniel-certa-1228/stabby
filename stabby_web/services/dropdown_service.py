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
    def get_blade_materials(self):
        return BladeMaterial.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_blade_shapes(self):
        return BladeShape.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_bonding_agents(self):
        return BondingAgent.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_brands(self):
        return Brand.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_countries(self):
        return Country.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_cutting_agents(self):
        return CuttingAgent.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_deployment_types(self):
        return DeploymentType.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_handle_materials(self):
        return HandleMaterial.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_knife_types(self):
        return KnifeType.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_lock_types(self):
        return LockType.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_lubricants(self):
        return Lubricant.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_steel_manufacturers(self):
        return SteelManufacturer.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_steel_types(self):
        return SteelType.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_units_of_measure(self):
        return UnitOfMeasure.objects.filter(is_active=1).order_by("name")

    @classmethod
    def get_vendors(self):
        return Vendor.objects.filter(is_active=1).order_by("name")
