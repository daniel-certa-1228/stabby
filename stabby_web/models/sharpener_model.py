from django.db import models
from .brand_model import Brand
from .country_model import Country
from .cutting_agent_model import CuttingAgent
from .bonding_agent_model import BondingAgent
from .lubricant_model import Lubricant
from .unit_of_measure_model import UnitOfMeasure
from django.contrib.auth.models import User

class Sharpener(models.Model):
    sharpener_id = models.AutoField(primary_key=True, db_column="sharpener_id")
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    brand_notes = models.TextField(null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )
    cutting_agent = models.ForeignKey(
        CuttingAgent, on_delete=models.SET_NULL, null=True, blank=True
    )
    bonding_agent = models.ForeignKey(
        BondingAgent, on_delete=models.SET_NULL, null=True, blank=True
    )
    lubricant = models.ForeignKey(
        Lubricant, on_delete=models.SET_NULL, null=True, blank=True
    )
    length = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=8)
    width = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=8)
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
