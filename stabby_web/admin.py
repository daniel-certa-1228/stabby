from django.contrib import admin

from .models import (
    BladeShape,
    BondingAgent,
    Country,
    CuttingAgent,
    DeploymentType,
    HandleMaterial,
    KnifeType,
    LockType,
    Lubricant,
    SteelType,
    UnitOfMeasure,
    Vendor,
    Brand,
    SteelManufacturer,
    BladeMaterial,
    Knife,
    Blade,
    Sharpener,
    WorkLog,
)


@admin.register(BladeShape)
class BladeShapeAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(BondingAgent)
class BondingAgentAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(CuttingAgent)
class CuttingAgentAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(DeploymentType)
class DeploymentTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(HandleMaterial)
class HandleMaterialAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(KnifeType)
class KnifeTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(LockType)
class LockTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(Lubricant)
class LubricantAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(SteelType)
class SteelTypeAdmin(admin.ModelAdmin):
    ordering = ["steel_type_id"]


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    ordering = ["uom_id"]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(SteelManufacturer)
class SteelManufacturerAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(BladeMaterial)
class BladeMaterialAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(Knife)
class KnifeAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(Blade)
class KnifeAdmin(admin.ModelAdmin):
    ordering = ["-is_main_blade", "knife_id"]


@admin.register(Sharpener)
class SharpenerAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(WorkLog)
class WorkLogAdmin(admin.ModelAdmin):
    ordering = ["-date"]
