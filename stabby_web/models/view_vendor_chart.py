from django.db import models


class ViewVendorChart(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    percentage = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=8
    )
    query_str = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "view_vendor_chart"
        managed = False
        abstract = True  # no primary key
