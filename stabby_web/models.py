from django.db import models
from django.contrib.auth.models import User


# Models with no foreign keys are in alphabetical order
class BladeShape(models.Model):
    blade_shape_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blade shape"
        verbose_name_plural = "blade shapes"

    def __str__(self):
        return self.name


class BondingAgent(models.Model):
    bonding_agent_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    is_friable = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "bonding agent"
        verbose_name_plural = "bonding agents"

    def __str__(self):
        return self.name


class Country(models.Model):
    country_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class CuttingAgent(models.Model):
    cutting_agent_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "cutting agent"
        verbose_name_plural = "cutting agents"

    def __str__(self):
        return self.name


class DeploymentType(models.Model):
    deployment_type_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "deployment type"
        verbose_name_plural = "deployment types"

    def __str__(self):
        return self.name


class HandleMaterial(models.Model):
    handle_material_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "handle material"
        verbose_name_plural = "handle materials"

    def __str__(self):
        return self.name


class KnifeType(models.Model):
    knife_type_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "knife type"
        verbose_name_plural = "knife types"

    def __str__(self):
        return self.name


class LockType(models.Model):
    lock_type_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "lock type"
        verbose_name_plural = "lock types"

    def __str__(self):
        return self.name


class Lubricant(models.Model):
    lubricant_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "lubricant"
        verbose_name_plural = "lubricants"

    def __str__(self):
        return self.name


class SteelType(models.Model):
    steel_type_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "steel type"
        verbose_name_plural = "steel types"

    def __str__(self):
        return self.name


class UnitOfMeasure(models.Model):
    uom_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "unit of measure"
        verbose_name_plural = "units of measure"

    def __str__(self):
        return self.name


class Vendor(models.Model):
    vendor_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "vendor"
        verbose_name_plural = "vendors"

    def __str__(self):
        return self.name


# Models with foreign keys are in necessary creation order
class Brand(models.Model):
    brand_id = models.BigIntegerField(primary_key=True, null=False)
    parent_brand = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="child_brands",
    )
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def __str__(self):
        return self.name


class SteelManufacturer(models.Model):
    steel_manufacturer_id = models.BigIntegerField(primary_key=True, null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "steel manufacturer"
        verbose_name_plural = "steel manufacturers"

    def __str__(self):
        return self.name


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


class Knife(models.Model):
    knife_id = models.AutoField(primary_key=True, db_column="knife_id")
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    brand_notes = models.TextField(null=True, blank=True)
    closed_length = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=8
    )
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, null=True)
    year_of_manufacture = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    year_of_purchase = models.CharField(max_length=50, null=True, blank=True)
    purchased_new = models.BooleanField(default=True, null=False)
    knife_type = models.ForeignKey(KnifeType, on_delete=models.SET_NULL, null=True)
    knife_type_notes = models.TextField(null=True, blank=True)
    blade_material = models.ForeignKey(
        BladeMaterial, on_delete=models.SET_NULL, null=True
    )
    blade_material_notes = models.TextField(null=True, blank=True)
    handle_material = models.ForeignKey(
        HandleMaterial, on_delete=models.SET_NULL, null=True
    )
    handle_material_notes = models.TextField(null=True, blank=True)
    lock_type = models.ForeignKey(LockType, on_delete=models.SET_NULL, null=True)
    lock_type_notes = models.TextField(null=True, blank=True)
    deployment_type = models.ForeignKey(
        DeploymentType, on_delete=models.SET_NULL, null=True
    )
    needs_work = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "knife"
        verbose_name_plural = "knives"

    def __str__(self):
        return self.name

    def number_of_blades(self):
        return self.blades.count()


class Blade(models.Model):
    blade_id = models.AutoField(primary_key=True, db_column="blade_id")
    knife = models.ForeignKey(Knife, on_delete=models.DO_NOTHING)
    length = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
    length_cutting_edge = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=8
    )
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, null=True)
    blade_shape = models.ForeignKey(BladeShape, on_delete=models.SET_NULL, null=True)
    blade_shape_notes = models.TextField(null=True, blank=True)
    has_half_stop = models.BooleanField(default=False, null=False)
    is_main_blade = models.BooleanField(default=True, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blade"
        verbose_name_plural = "blades"

    def __str__(self):
        return f"Blade - {self.knife.name}"


class Sharpener(models.Model):
    sharpener_id = models.AutoField(primary_key=True, db_column="sharpener_id")
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    brand_notes = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    cutting_agent = models.ForeignKey(
        CuttingAgent, on_delete=models.SET_NULL, null=True
    )
    bonding_agent = models.ForeignKey(
        BondingAgent, on_delete=models.SET_NULL, null=True
    )
    lubricant = models.ForeignKey(Lubricant, on_delete=models.SET_NULL, null=True)
    length = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
    width = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "sharpener"
        verbose_name_plural = "sharpeners"

    def __str__(self):
        return self.name


class WorkLog(models.Model):
    work_log_id = models.AutoField(primary_key=True, db_column="work_log_id")
    knife = models.ForeignKey(Knife, on_delete=models.SET_NULL, null=True)
    sharpener = models.ForeignKey(Sharpener, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=False)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "work log"
        verbose_name_plural = "work logs"

    def __str__(self):
        return self.description


# VIEWS
class ViewKnifeGrid(models.Model):
    knife_id = models.BigIntegerField(primary_key=True, db_column="knife_id")
    knife = models.CharField(max_length=255, null=True)
    knife_type = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255, null=True)
    num_of_blades = models.IntegerField(null=True)
    blade_material = models.CharField(max_length=255, null=True)
    handle_material = models.CharField(max_length=255, null=True)
    lock_type = models.CharField(max_length=255, null=True)
    deployment_type = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    vendor = models.CharField(max_length=255, null=True)
    needs_work = models.BooleanField(null=False)
    is_active = models.BooleanField(null=False)
    user_id = models.BigIntegerField(null=False)

    class Meta:
        db_table = "view_knife_grid"
        managed = False
