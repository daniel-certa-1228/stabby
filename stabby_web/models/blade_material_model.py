from django.db import models
from .steel_type_model import SteelType
from .steel_manufacturer_model import SteelManufacturer

class BladeMaterial(models.Model):
    blade_material_id = models.BigIntegerField(primary_key=True, null=False)
    steel_type = models.ForeignKey(SteelType, on_delete=models.SET_NULL, null=True)
    steel_manufacturer = models.ForeignKey(
        SteelManufacturer, on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blade material"
        verbose_name_plural = "blade materials"

    def __str__(self):
        return self.name