from django.db import models
from .blade_shape_model import BladeShape
from .knife_model import Knife
from .unit_of_measure_model import UnitOfMeasure


class Blade(models.Model):
    blade_id = models.AutoField(primary_key=True, db_column="blade_id")
    knife = models.ForeignKey(Knife, on_delete=models.DO_NOTHING)
    length = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=8)
    length_cutting_edge = models.DecimalField(
        null=True, blank=True, decimal_places=4, max_digits=8
    )
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, null=True)
    blade_shape = models.ForeignKey(
        BladeShape, on_delete=models.SET_NULL, null=True, blank=True
    )
    blade_shape_notes = models.TextField(null=True, blank=True)
    has_half_stop = models.BooleanField(default=False, null=False)
    is_main_blade = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blade"
        verbose_name_plural = "blades"

    def __str__(self):
        return f"Blade - {self.knife.name}"

    def save(self, *args, **kwargs):
        if self.is_main_blade:
            Blade.objects.filter(knife_id=self.knife_id).exclude(
                blade_id=self.blade_id
            ).update(is_main_blade=False)

        super().save(*args, **kwargs)
