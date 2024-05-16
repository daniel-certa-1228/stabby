from django.db import models
from .knife_model import Knife
from .sharpener_model import Sharpener

class WorkLog(models.Model):
    work_log_id = models.AutoField(primary_key=True, db_column="work_log_id")
    knife = models.ForeignKey(Knife, on_delete=models.SET_NULL, null=True)
    sharpener = models.ForeignKey(Sharpener, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=False)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "work log"
        verbose_name_plural = "work logs"

    def __str__(self):
        return self.description