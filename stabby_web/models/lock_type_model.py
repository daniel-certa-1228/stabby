from django.db import models

class LockType(models.Model):
    lock_type_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "lock type"
        verbose_name_plural = "lock types"

    def __str__(self):
        return self.name