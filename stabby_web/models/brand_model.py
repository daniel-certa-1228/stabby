from django.db import models

class Brand(models.Model):
    brand_id = models.BigIntegerField(primary_key=True, null=False)
    parent_brand = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="child_brands",
    )
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"

    def __str__(self):
        return self.name
