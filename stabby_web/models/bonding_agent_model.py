from django.db import models

class BondingAgent(models.Model):
    bonding_agent_id = models.BigIntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    is_friable = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "bonding agent"
        verbose_name_plural = "bonding agents"

    def __str__(self):
        return self.name