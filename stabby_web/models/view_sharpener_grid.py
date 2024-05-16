from django.db import models

class ViewSharpenerGrid(models.Model):
    sharpener_id = models.AutoField(primary_key=True, db_column="sharpener_id")
    sharpener = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    cutting_agent = models.CharField(max_length=255)
    bonding_agent = models.CharField(max_length=255)
    length = models.CharField(max_length=20)
    width = models.CharField(max_length=20)
    country = models.CharField(max_length=255, null=True)
    is_friable = models.BooleanField(null=False)
    is_active = models.BooleanField(null=False)
    user_id = models.BigIntegerField(null=False)

    class Meta:
        db_table = "view_sharpener_grid"
        managed = False