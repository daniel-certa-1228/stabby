from django.db import models
from .knife_model import Knife
from .sharpener_model import Sharpener
from django_resized import ResizedImageField


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True, db_column="photo_id")
    photo = ResizedImageField(size=[2000, 1500], upload_to="images/", quality=85)
    name = models.CharField(max_length=100, null=True, blank=True)
    knife = models.ForeignKey(Knife, on_delete=models.SET_NULL, null=True)
    sharpener = models.ForeignKey(Sharpener, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "photos"

    def __str__(self):
        return self.name if self.name else f"Photo {self.photo_id}"
