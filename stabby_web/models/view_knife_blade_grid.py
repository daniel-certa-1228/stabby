from django.db import models


class ViewKnifeBladeGrid(models.Model):
    knife_id = models.BigIntegerField(primary_key=True, db_column="knife_id")
    blade_shape_id = models.BigIntegerField(null=False)
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
    purchased_new = models.BooleanField(null=False)
    is_active = models.BooleanField(null=False)
    create_date = models.DateTimeField(null=False)
    user_id = models.BigIntegerField(null=False)
    has_pocket_clip = models.BooleanField(null=False)

    class Meta:
        db_table = "view_knife_blade_grid"
        managed = False
