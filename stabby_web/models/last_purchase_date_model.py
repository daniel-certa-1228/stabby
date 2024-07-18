from django.db import models


class LastPurchaseDate(models.Model):
    last_purchase_date_id = models.BigIntegerField(primary_key=True, null=False)
    last_purchase_date = models.DateField()

    class Meta:
        verbose_name = "last_purchase_date"

    def __str__(self):
        return self.name
