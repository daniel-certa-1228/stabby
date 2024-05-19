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
    Photo
)


@admin.register(BladeShape)
class BladeShapeAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(BondingAgent)
class BondingAgentAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(CuttingAgent)
class CuttingAgentAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(DeploymentType)
class DeploymentTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(HandleMaterial)
class HandleMaterialAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(KnifeType)
class KnifeTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(LockType)
class LockTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(Lubricant)
class LubricantAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(SteelType)
class SteelTypeAdmin(admin.ModelAdmin):
    ordering = ["steel_type_id"]
    list_display = ["name", "is_active"]


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    ordering = ["uom_id"]
    list_display = ["name", "is_active"]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "is_active"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "parent_brand", "is_active"]


@admin.register(SteelManufacturer)
class SteelManufacturerAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "country", "is_active"]


@admin.register(BladeMaterial)
class BladeMaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "steel_type", "steel_manufacturer", "is_active"]


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
   
    
@admin.register(Photo)
class WorkLogAdmin(admin.ModelAdmin):
    ordering = ["name", "-create_date"]
