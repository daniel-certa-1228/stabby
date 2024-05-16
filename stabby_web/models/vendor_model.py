from django.db import models

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