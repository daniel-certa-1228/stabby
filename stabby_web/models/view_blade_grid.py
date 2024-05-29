from django.db import models


class ViewBladeGrid(models.Model):
    blade_id = models.BigIntegerField(primary_key=True, db_column="blade_id")
    knife_id = models.BigIntegerField(blank=False, null=False)
    blade_shape = models.CharField(max_length=100)
    length = models.CharField(max_length=20)
    length_cutting_edge = models.CharField(max_length=20)
    has_half_stop = models.BooleanField(default=False, null=False)
    is_main_blade = models.BooleanField(default=True, null=False)
    is_active = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = "view_blade_grid"
        managed = False
