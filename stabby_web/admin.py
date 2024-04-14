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

admin.site.register(BladeShape)
admin.site.register(BondingAgent)
admin.site.register(Country)
admin.site.register(CuttingAgent)
admin.site.register(DeploymentType)
admin.site.register(HandleMaterial)
admin.site.register(KnifeType)
admin.site.register(LockType)
admin.site.register(Lubricant)
admin.site.register(SteelType)
admin.site.register(UnitOfMeasure)
admin.site.register(Vendor)
admin.site.register(Brand)
admin.site.register(SteelManufacturer)
admin.site.register(BladeMaterial)
admin.site.register(Knife)
admin.site.register(Blade)
admin.site.register(Sharpener)
admin.site.register(WorkLog)
