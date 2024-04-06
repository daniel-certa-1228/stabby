from django.db import models


# Create your models here.


class UnitOfMeasure(models.Model):
    uom_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class BladeShape(models.Model):
    blade_shape_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class SteelType(models.Model):
    steel_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class Vendor(models.Model):
    vendor_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class KnifeType(models.Model):
    knife_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class LockType(models.Model):
    lock_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()


class DeploymentType(models.Model):
    deployment_type_id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return super().__name__()
