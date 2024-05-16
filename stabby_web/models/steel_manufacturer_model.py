from django.db import models
from .country_model import Country

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