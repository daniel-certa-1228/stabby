from django.db import models


class ViewBladeShapeChart(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    percentage = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=8
    )
    blade_shape_id = models.BigIntegerField(null=False)

    class Meta:
        db_table = "view_blade_shape_chart"
        managed = False
        abstract = True  # no primary key
