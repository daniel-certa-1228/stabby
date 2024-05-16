from django.db import models

class SteelType(models.Model):
    steel_type_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "steel type"
        verbose_name_plural = "steel types"

    def __str__(self):
        return self.name