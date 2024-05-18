from django.shortcuts import get_object_or_404
from django.utils import timezone
from stabby_web.models.photo_model import Photo


class PhotoService:
  
    @classmethod
    def delete_photo(cls, photo):
        photo.is_active = False

        return photo
      
    @classmethod
    def get_knife_photos(cls, knife_id):
        queryset = Photo.objects.filter(is_active=True, knife_id=knife_id).order_by(
            "-create_date"
        )

        return list(queryset.values())
      
    @classmethod
    def get_sharpener_photos(cls, sharpener_id):
        queryset = Photo.objects.filter(is_active=True, sharpener_id=sharpener_id).order_by(
            "-create_date"
        )

        return list(queryset.values())
      
    @classmethod
    def get_photo_detail(cls, photo_id):
        return get_object_or_404(Photo, photo_id=photo_id)
      
    @classmethod
    def map_photo_form_data(cls, form, knife=None, sharpener=None, photo=None):
        if photo == None:
            photo = Photo()
            photo.create_date = timezone.now()
            photo.knife = knife
            photo.sharpener = sharpener

        photo.edit_date = timezone.now()
        photo.photo = form.cleaned_data["photo"]
        photo.name = form.cleaned_data["name"]

        return photo
      
    @classmethod
    def save_photo(cls, photo):
        return photo.save()