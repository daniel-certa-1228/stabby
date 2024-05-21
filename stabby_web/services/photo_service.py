from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import Photo


class PhotoService:

    @classmethod
    def delete_photo(cls, photo):
        photo.is_active = False

        return photo

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
            photo.photo = form.cleaned_data["photo"]

        photo.edit_date = timezone.now()
        photo.description = form.cleaned_data["description"]

        return photo

    @classmethod
    def save_photo(cls, photo):
        return photo.save()
