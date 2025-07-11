import datetime
from django.shortcuts import get_object_or_404
from ..models import Photo, Knife, Sharpener


class PhotoService:

    @classmethod
    def delete_photo(cls, photo: Photo):
        photo.is_active = False

        return photo

    @classmethod
    def get_photo_detail(cls, photo_id: int):
        return get_object_or_404(Photo, photo_id=photo_id)

    @classmethod
    def map_photo_form_data(
        cls,
        form,
        now: datetime,
        knife: Knife = None,
        sharpener: Sharpener = None,
        photo: Photo = None,
    ):
        if photo == None:
            photo = Photo()
            photo.create_date = now
            photo.knife = knife
            photo.sharpener = sharpener
            photo.brand = form.cleaned_data["brand"]
            photo.photo = form.cleaned_data["photo"]

        photo.edit_date = now
        photo.description = form.cleaned_data["description"]

        return photo

    @classmethod
    def save_photo(cls, photo: Photo):
        return photo.save()
