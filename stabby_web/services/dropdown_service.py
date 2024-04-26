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
        queryset = BladeMaterial.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_blade_shapes(self):
        queryset = BladeShape.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_bonding_agents(self):
        queryset = BondingAgent.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_brands(self):
        queryset = Brand.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_countries(self):
        queryset = Country.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_cutting_agents(self):
        queryset = CuttingAgent.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_deployment_types(self):
        queryset = DeploymentType.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_handle_materials(self):
        queryset = HandleMaterial.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_knife_types(self):
        queryset = KnifeType.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_lock_types(self):
        queryset = LockType.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_lubricants(self):
        queryset = Lubricant.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_steel_manufacturers(self):
        queryset = SteelManufacturer.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_steel_types(self):
        queryset = SteelType.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_units_of_measure(self):
        queryset = UnitOfMeasure.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())

    @classmethod
    def get_vendors(self):
        queryset = Vendor.objects.filter(is_active=1).order_by("name")

        return list(queryset.values())
