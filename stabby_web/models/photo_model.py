from io import BytesIO
from PIL import Image
from django.db import models
from .brand_model import Brand
from .knife_model import Knife
from .sharpener_model import Sharpener
from django.core.files.base import ContentFile


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True, db_column="photo_id")
    photo = models.ImageField(upload_to="images/")
    description = models.TextField(null=True, blank=True)
    knife = models.ForeignKey(
        Knife, related_name="photos", on_delete=models.SET_NULL, null=True, blank=True
    )
    sharpener = models.ForeignKey(
        Sharpener,
        related_name="photos",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        related_name="photos",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "photos"
        ordering = ["create_date"]

    def save(self, *args, **kwargs):
        # Open the image file
        img = Image.open(self.photo)

        # Check the resolution of the image
        if img.width > 1200 or img.height > 900:
            # Resize the image only if it's larger than the desired size
            img = img.resize((1200, 900), Image.LANCZOS)
            output = BytesIO()
            img.save(output, format="JPEG", quality=85)
            output.seek(0)

            # Replace the old photo with the resized one
            self.photo = ContentFile(output.read(), self.photo.name)

        # Call the parent class's save method to save the model
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description if self.description else f"Photo {self.photo_id}"
