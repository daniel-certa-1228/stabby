from dataclasses import dataclass
from typing import List
from .photo_dto import PhotoDTO


@dataclass
class BrandPhotoDTO:
    brand_id: int
    brand_name: str
    photos: List[PhotoDTO]
