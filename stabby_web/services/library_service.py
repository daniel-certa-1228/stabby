from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from stabby_web.dtos import BrandPhotoDTO, PhotoDTO
from ..models import Brand, Photo


class LibraryService:

    @classmethod
    def get_photos_grouped_by_brand(cls):
        brands_with_photos = (
            Brand.objects.annotate(
                photo_count=Count("photos", filter=Q(photos__is_active=True))
            )
            .filter(photo_count__gt=0)
            .prefetch_related("photos")
        )

        brand_photos_dtos = []

        for brand in brands_with_photos:
            photos = brand.photos.filter(is_active=True)

            photo_dtos = [
                PhotoDTO(
                    photo_id=photo.photo_id,
                    photo_url=photo.photo.url,
                    description=photo.description,
                )
                for photo in photos
            ]

            brand_photos_dtos.append(
                BrandPhotoDTO(
                    brand_id=brand.brand_id, brand_name=brand.name, photos=photo_dtos
                )
            )

        return brand_photos_dtos
