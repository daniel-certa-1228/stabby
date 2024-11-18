from dataclasses import dataclass
from typing import List
from stabby_web.dtos import PhotoDTO


@dataclass
class BrandPhotoDTO:
    brand_id: int
    brand_name: str
    photos: List[PhotoDTO]
