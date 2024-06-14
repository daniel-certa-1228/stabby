from django.db import models
from .blade_material_model import BladeMaterial
from .brand_model import Brand
from .country_model import Country
from .deployment_type_model import DeploymentType
from .handle_material_model import HandleMaterial
from .knife_type_model import KnifeType
from .lock_type_model import LockType
from .unit_of_measure_model import UnitOfMeasure
from django.contrib.auth.models import User
from .vendor_model import Vendor


class Knife(models.Model):
    knife_id = models.AutoField(primary_key=True, db_column="knife_id")
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    brand_notes = models.TextField(null=True, blank=True)
    closed_length = models.DecimalField(
        null=True, blank=True, decimal_places=4, max_digits=8
    )
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, null=True)
    year_of_manufacture = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    year_of_purchase = models.CharField(max_length=50, null=True, blank=True)
    purchased_new = models.BooleanField(default=True, null=False)
    knife_type = models.ForeignKey(
        KnifeType, on_delete=models.SET_NULL, null=True, blank=True
    )
    knife_type_notes = models.TextField(null=True, blank=True)
    blade_material = models.ForeignKey(
        BladeMaterial, on_delete=models.SET_NULL, null=True, blank=True
    )
    blade_material_notes = models.TextField(null=True, blank=True)
    handle_material = models.ForeignKey(
        HandleMaterial, on_delete=models.SET_NULL, null=True, blank=True
    )
    handle_material_notes = models.TextField(null=True, blank=True)
    lock_type = models.ForeignKey(
        LockType, on_delete=models.SET_NULL, null=True, blank=True
    )
    lock_type_notes = models.TextField(null=True, blank=True)
    deployment_type = models.ForeignKey(
        DeploymentType, on_delete=models.SET_NULL, null=True, blank=True
    )
    needs_work = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def number_of_blades(self):
        return self.blades.filter(is_active=1).count()

    class Meta:
        verbose_name = "knife"
        verbose_name_plural = "knives"

    def __str__(self):
        return self.name
