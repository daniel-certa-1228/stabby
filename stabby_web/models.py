from django.db import models


# Create your models here.


class UnitOfMeasure(models.Model):
    uom_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "unit of measure"
        verbose_name_plural = "units of measure"

    def __str__(self):
        return super().__name__()


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return super().__name__()


class BladeShape(models.Model):
    blade_shape_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blade shape"
        verbose_name_plural = "blade shapes"

    def __str__(self):
        return super().__name__()


class SteelType(models.Model):
    steel_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "steel type"
        verbose_name_plural = "steel types"

    def __str__(self):
        return super().__name__()


class Vendor(models.Model):
    vendor_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "vendor"
        verbose_name_plural = "vendors"

    def __str__(self):
        return super().__name__()


class KnifeType(models.Model):
    knife_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "knife type"
        verbose_name_plural = "knife types"

    def __str__(self):
        return super().__name__()


class LockType(models.Model):
    lock_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "lock type"
        verbose_name_plural = "lock types"

    def __str__(self):
        return super().__name__()


class DeploymentType(models.Model):
    deployment_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "deployment type"
        verbose_name_plural = "deployment types"

    def __str__(self):
        return super().__name__()


class HandleMaterial(models.Model):
    handle_material_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "handle material"
        verbose_name_plural = "handle materials"

    def __str__(self):
        return super().__name__()


class CuttingAgent(models.Model):
    cutting_agent_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "cutting agent"
        verbose_name_plural = "cutting agents"

    def __str__(self):
        return super().__name__()


class Lubricant(models.Model):
    lubricant_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "lubricant"
        verbose_name_plural = "lubricants"

    def __str__(self):
        return super().__name__()


class BondingAgent(models.Model):
    bonding_agent_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    is_friable = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "bonding agent"
        verbose_name_plural = "bonding agents"

    def __str__(self):
        return super().__name__()


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True, unique=True, null=False)
    parent_brand_id = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="child_brands",
    )
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def __str__(self):
        return super().__name__()


class SteelManufacturer(models.Model):
    steel_manufacturer_id = models.IntegerField(
        primary_key=True, unique=True, null=False
    )
    country_id = models.IntegerField(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="country_id",
    )
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "steel manufacturer"
        verbose_name_plural = "steel manufacturers"

    def __str__(self):
        return super().__name__()


class BladeMaterial(models.Model):
    blade_material_id = models.IntegerField(primary_key=True, unique=True, null=False)
    steel_type_id = models.IntegerField(
        SteelType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="steel_type_id",
    )
    steel_manufacturer_id = models.IntegerField(
        SteelManufacturer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="steel_manufacturer_id",
    )
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blade material"
        verbose_name_plural = "blade materials"

    def __str__(self):
        return super().__name__()
