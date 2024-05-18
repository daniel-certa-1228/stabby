from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import (
    WorkLog,
)


class PhotoService:
  
    @classmethod
    def delete_photo(cls, photo):
        photo.is_active = False

        return photo
      
    @classmethod
    