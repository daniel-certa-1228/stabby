from django.db import models

class Country(models.Model):
    country_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name